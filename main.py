"""

Protejo Integrador Ártemis

É o projeto integrador desenvolvido por alunos do 2° ano de informática vespertino
do Instituto Federal de Educação, Ciência e Tecnologia de Rondônia Campus Porto Velho
Calama para obtenção de notas nas disciplinas de Banco de Dados, Fundamentos de Análises 
de Sistemas, Linguagem de Programação e Programação Orientada a Objetos. O objetivo 
deste projeto é desenvolver as habilidades trabalhadas em cada uma dessas disciplinas 
criando um planner que auxilie na organização de discentes e docentes.

Integrantes:s

- Marcos Reis Dutra
- João Pedro Monteiro Ferreira
- Nicolle Cristini Dias
- Isabella Cristina Queiroz

"""

# Importando biblioteca do sistema
import os


# Importando Banco de dados
import banco

# Importando as classes a serem utilizadas
from view import usuario, agendamento

# Importando o sqlite3
import sqlite3 as lite
import senhaValida

# Importando o Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import StringVar


# Importando tkcalendar
from tkcalendar import Calendar
from tkcalendar import DateEntry

# Importando a função de envio de email
from recuperarSenhaPorEmail import enviar_email

# Declaração de variaveis globais
conexao = lite.connect('Bancodedados.db')
global usuario_atual
global codigo
global tree

class NomeVazioError(Exception):
  pass

class CodigoError(Exception):
  pass


# Caso o banco de dados não existe ele será criado
if not os.path.isfile("Bancodedados.db"):
  os.system('python banco.py')


def tela(nome="Planner Ártemis"):
  tela = Tk()
  tela.title(nome)
  tela.geometry("900x450+610+153")
  tela.resizable(width=False, height=False)
  logo = PhotoImage(file = 'images/logo.png')
  tela.iconphoto(False, logo)
  return tela


# Criando janela inicial
def tela_inicial():
  # Criando a tela
  janelaInicial = tela()


  # Carregando as imagens
  img_telainicial = PhotoImage(file='images/fundos/TelaInicial.png')
  img_botaologin = PhotoImage(file='images/botoes/BotaoLogin.png')
  img_botaocadastro = PhotoImage(file='images/botoes/BotaoCadastro.png')
  img_botaosobre = PhotoImage(file='images/botoes/BotaoSobre.png')


  # Criação da/das label/s
  lab_fundo = Label(janelaInicial, image=img_telainicial)
  lab_fundo.pack()

  
  # Criação de botões
  bt_login = Button(janelaInicial, bd=0, image=img_botaologin, command=lambda: [janelaInicial.destroy(), tela_login()])
  bt_login.place(width=150, height=50, x=228, y=322)

  
  bt_cadastro = Button(janelaInicial, bd=0, image=img_botaocadastro, command=lambda: [janelaInicial.destroy(), tela_cadastro()])
  bt_cadastro.place(width=150, height=50, x=522, y=322)

  
  bt_sobre = Button(janelaInicial, bd=0, image=img_botaosobre, command=lambda: [janelaInicial.destroy(), tela_sobre()])
  bt_sobre.place(width=120, height=40, x=760, y=13)

  
  janelaInicial.mainloop()


def tela_sobre():
  # Criando a tela
  janelaSobre = tela('Planner Ártemis - Sobre')

  
  # Carregando as imagens
  img_telasobre = PhotoImage(file='images/fundos/TelaSobre.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')

  
  # Criação da/das label/s
  lab_fundo = Label(janelaSobre, image=img_telasobre)
  lab_fundo.pack()

  
  # Criação dos botões
  bt_voltar = Button(janelaSobre, bd=0, image=img_botaovoltar, command=lambda: [janelaSobre.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  
  janelaSobre.mainloop()


def tela_login():
  # Criando a tela
  janelaLogin = tela('Planner Ártemis - Login')

  
  # Carregando as imagens
  img_telalogin = PhotoImage(file='images/fundos/TelaLogin.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoinicia = PhotoImage(file='images/botoes/BotaoIniciarsessao.png')
  img_btesquece = PhotoImage(file='images/botoes/BotaoEsquece.png')
  img_botaocadastro = PhotoImage(file='images/botoes/BotaoRcadastro.png')

  
  # Criação da/das label/s  
  lab_fundo = Label(janelaLogin, image=img_telalogin)
  lab_fundo.pack()

  
  # Configurando entrada de dados
  esconda_senha = StringVar()
  en_username = Entry(janelaLogin, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  
  en_senha = Entry(janelaLogin, textvariable=esconda_senha, show='*', bd=2, font=("Calibri", 15), justify=CENTER)
  en_senha.place(width=392, height=44, x=253, y=235)

  
  # Criação dos botões
  bt_voltar = Button(janelaLogin, bd=0, image=img_botaovoltar, command=lambda: [janelaLogin.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  
  bt_cadastro = Button(janelaLogin, bd=0, image=img_botaocadastro, command=lambda: [janelaLogin.destroy(), tela_cadastro()])
  bt_cadastro.place(width=130, height=30, x=517, y=298)

  
  bt_iniciasessao = Button(janelaLogin, 
                           bd=0, 
                           image=img_botaoinicia, 
                           command=lambda: [janelaLogin.destroy(),
                                            tela_agendamentos()] 
                           if login_valido(en_username.get(), en_senha.get()) else
                           [messagebox.showerror('ERRO','Usuário e/ou senha errados'),
                            en_username.delete(0, 'end'),
                            en_senha.delete(0, 'end')])
  bt_iniciasessao.place(width=150, height=50, x=698, y=365)

  
  bt_esquecesenha = Button(janelaLogin, bd=0, image=img_btesquece, command=lambda: [janelaLogin.destroy(), tela_ajuda()])
  bt_esquecesenha.place(width=130, height=30, x=252, y=298)

  
  janelaLogin.mainloop()


def tela_cadastro():
  # Criando a tela
  janelaCadastro = tela('Planner Ártemis - Cadastro')

  
  # Carregando as imagens
  img_telacadastro = PhotoImage(file='images/fundos/Telacadastro.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoconcluir = PhotoImage(file='images/botoes/BotaoConcluir.png')

  # Criação da/das label/s  
  lab_fundo = Label(janelaCadastro, image=img_telacadastro)
  lab_fundo.pack()

  
  # Configurando entrada de dados
  en_username = Entry(janelaCadastro, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  en_senha = Entry(janelaCadastro, textvariable=StringVar(), show='*', bd=2, font=("Calibri", 15), justify=CENTER)
  en_senha.place(width=392, height=44, x=253, y=235)

  en_local = Entry(janelaCadastro, bd=2, font=("Calibri", 15), justify=CENTER)
  en_local.place(width=392, height=44, x=253, y=333)

  # Logica para logar usuario
  def logar_usuario(nome,senha,backup):
    global usuario_atual
    usuario_atual = usuario(nome, senha, backup)

    
  # Criação dos botões
  bt_voltar = Button(janelaCadastro, bd=0, image=img_botaovoltar, command=lambda: [janelaCadastro.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  
  bt_concluir = Button( janelaCadastro, bd=0, image=img_botaoconcluir, command=lambda: [logar_usuario(en_username.get(), en_senha.get(), en_local.get()),janelaCadastro.destroy(), tela_agendamentos()] if usuario.cadastro_user(en_username.get(), en_senha.get(), en_local.get()) else [])
  bt_concluir.place(width=150, height=50, x=698, y=365)

  
  janelaCadastro.mainloop()


def tela_ajuda():
  # Criando a tela
  janelaAjuda = tela('Planner Ártemis - Ajuda')

  
  # Carregando as imagens
  img_telaajuda = PhotoImage(file='images/fundos/TelaAjuda.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaorecupera = PhotoImage(file='images/botoes/BotaoEnviarCodigo.png')

  
  # Criação da/das label/s  
  lab_fundo = Label(janelaAjuda, image=img_telaajuda)
  lab_fundo.pack()

  
  # Configurando entrada de dados
  en_username = Entry(janelaAjuda, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  en_email = Entry(janelaAjuda, bd=2, font=("Calibri", 15), justify=CENTER)
  en_email.place(width=392, height=44, x=253, y=235)

  # Criação dos botões
  bt_voltar = Button(janelaAjuda, bd=0, image=img_botaovoltar, command=lambda: [janelaAjuda.destroy(), tela_login()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  bt_recuperar = Button(janelaAjuda, 
                        bd=0, 
                        image=img_botaorecupera, 
                        command=lambda: 
                        [ 
                          messagebox.showinfo( title="SUCESSO", message=f'Um código foi enviado! Olhe seu email'),
                          salvarCodigo(enviar_email(en_email.get(),en_username.get())),
                          janelaAjuda.destroy(),
                          tela_enviarcodigo(),
                        ] 
                        if email_valido(en_username.get(), en_email.get()) else 
                        [
                          messagebox.showerror(title='ERRO', message='A resposta está errada!')
                        ],)
  bt_recuperar.place(width=200, height=50, x=350, y=341)


  # Logica de validação de email
  def email_valido(username, backup):
    global usuario_atual
    if username and backup:
      if usuario.get_email(username) != backup:
        return False
      else:
        user = usuario.get_usuario(username)
        usuario_atual = usuario(user[0][1], user[0][2], user[0][3])
        return True
    else:
      return False

  
  janelaAjuda.mainloop()

def salvarCodigo(codigo_temp: bool or str) -> None:
  global codigo
  if not codigo_temp:
    janelaAjuda.destroy()
    tela_ajuda()
  codigo = codigo_temp

def tela_enviarcodigo():
  global codigo
  janelaEnviocodigo = tela('Planner Ártemis - Código de verificação')
  img_telaaltera = PhotoImage(file='images/fundos/TelaAlterarSenha1.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoverificar = PhotoImage(file='images/botoes/BotaoVerificarCodigo.png')

  lab_fundo = Label(janelaEnviocodigo, image= img_telaaltera)
  lab_fundo.pack()

  # Configurando entrada de dados
  en_code = Entry(janelaEnviocodigo, bd=2, font=("Calibri", 15), justify=CENTER)
  en_code.place(width=392, height=44, x=252, y=210)

  def verificaCodigo():
    print("verifica codigo")
    codi = en_code.get()
    codi = codi.upper()
    try:
      if codi != codigo:
        raise CodigoError
    except CodigoError: 
      messagebox.showerror('Erro', 'O código está Incorreto!')
    else:
      janelaEnviocodigo.destroy()
      tela_alterarsenha()
       
      
  bt_voltar = Button(janelaEnviocodigo, 
                     bd=0, 
                     image=img_botaovoltar, 
                     command=lambda: [janelaEnviocodigo.destroy(),tela_login()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  bt_verificar = Button(janelaEnviocodigo, bd=0, image=img_botaoverificar, command=lambda: [verificaCodigo()])
  bt_verificar.place(width=200, height=50, x=360, y=355)

  janelaEnviocodigo.mainloop()

def tela_alterarsenha():
  janelaAltera = tela("Planner Ártemis - Alterar Senha")
  
  img_telaaltera = PhotoImage(file='images/fundos/TelaAlterarSenha2.png')
  img_botaoredefinir = PhotoImage(file='images/botoes/BotaoRedefinirSenha.png')

  lab_fundo = Label(janelaAltera, image = img_telaaltera)
  lab_fundo.pack()
  
  en_novasenha = Entry(janelaAltera, bd=2, font=("Calibri", 15), textvariable=StringVar(), show='*', justify=CENTER)
  en_novasenha.place(width=392, height=44, x=252, y=210)

  id = usuario_atual.get_id()
  bt_redefinirsenha = Button(janelaAltera, 
                             bd=0, 
                             image = img_botaoredefinir, 
                             command=lambda: [usuario.alterar_senha(en_novasenha.get(), id),
                                              messagebox.showinfo(title='SUCESSO', message='Senha Alterada com sucesso!'),
                                              janelaAltera.destroy(),
                                              tela_login()] if senhaValida.senhaForte(en_novasenha.get()) else []
                            )
  bt_redefinirsenha.place(width=200, height=50, x=360, y=355)  

  janelaAltera.mainloop()
  
def tela_agendamentos():
  # Criando a tela
  janelaAgenda = tela('Planner Ártemis - Agendamentos')

  # Carregando as imagens
  img_cima = PhotoImage(file='images/fundos/cima.png')
  img_lado = PhotoImage(file='images/fundos/lado.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoinserir = PhotoImage(file='images/botoes/BotaoInserir.png')
  img_botaoatualizar = PhotoImage(file='images/botoes/BotaoAtualizar.png')
  img_botaodeletar = PhotoImage(file='images/botoes/BotaoDeletar.png')
  img_botaoconfirma = PhotoImage(file='images/botoes/BotaoConfirmar.png')


  # Criação da/das label/s  
  lab_cima = Label(janelaAgenda, image=img_cima)
  lab_cima.pack()
  lab_lado = Label(janelaAgenda, image=img_lado)
  lab_lado.pack(side=LEFT)

  
  # Configurando o Frame que em ocorrerá a visualização da tabela
  branco = '#000000'
  direita = Frame(janelaAgenda, width=577, height=500, bd=1, bg=branco, relief="raise")
  direita.pack(padx=1, pady=0)

  
  # Configurando entrada de dados
  en_nome = Entry(janelaAgenda, bd=2, font=("Calibri", 12), justify=CENTER)
  en_nome.place(width=210, height=30, x=20, y=123)

  e_cal = DateEntry(janelaAgenda, width=21, background='darkblue', foreground='white', borderwidth=4, year=2022)
  e_cal.place(x=24, y=189)

  en_descricao = Text(janelaAgenda, bd=2, font=("Calibri", 12))
  en_descricao.place(width=210, height=80, x=20, y=252)


  # Logica para inserir Agendamentos
  def inserir():
    global usuario_atual
    nome = en_nome.get()
    dia = e_cal.get()
    descricao = en_descricao.get(1.0, 'end')
    id = usuario_atual.get_id()
    
    lista = agendamento(None, nome, dia, descricao, id)
    try:
      if nome == '':
        raise NomeVazioError  
    except NomeVazioError:
      messagebox.showerror('Erro', 'O nome não pode ser vazio')
    else:
      agendamento.inserir_info(lista)
      messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

      en_nome.delete(0, 'end')
      e_cal.delete(0, 'end')
      en_descricao.delete(1.0, 'end')
    for widget in direita.winfo_children():
      widget.destroy()

    mostrar()

    
  # Logica para atualizar agendamentos
  def atualizar():
    try:
      treev_dados = tree.focus()
      treev_dicionario = tree.item(treev_dados)
      tree_lista = treev_dicionario['values']

      valor_id = tree_lista[0]

      en_nome.delete(0, 'end')
      e_cal.delete(0, 'end')
      en_descricao.delete(1.0, 'end')

      en_nome.insert(0, tree_lista[1])
      e_cal.insert(0, tree_lista[2])
      en_descricao.insert(1.0, tree_lista[3])

      def update():
        nome = en_nome.get()
        dia = e_cal.get()
        descricao = en_descricao.get(1.0, 'end')

        lista = agendamento(None ,nome, dia, descricao, valor_id)
        try:
          if nome == '':
            raise NomeVazioError  
        except NomeVazioError:
          messagebox.showerror('Erro', 'O nome não pode ser vazio')
        else:
          agendamento.atualizar_info(lista)
          messagebox.showinfo('Sucesso',
                              'Os dados foram atualizados com sucesso')

          en_nome.delete(0, 'end')
          e_cal.delete(0, 'end')
          en_descricao.delete(1.0, 'end')

        for widget in direita.winfo_children():
          widget.destroy()

        mostrar()

      # Botão Confirmar atualizações
      b_confirmar = Button(
        janelaAgenda,
        bd=0,
        image=img_botaoconfirma,
        command=lambda: [update(), b_confirmar.destroy()])
      b_confirmar.place(width=80, height=25, x=100, y=370)

    except IndexError:
      messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

  # Logica para deletar agendamentos
  def deletar():
    global agendamentos
    try:
      treev_dados = tree.focus()
      treev_dicionario = tree.item(treev_dados)
      tree_lista = treev_dicionario['values']
      
      indice = tree_lista[0]-1
      
      agendamentos[indice].deletar_info()
      messagebox.showinfo('Sucesso',
                          'Os dados foram deletados da tabela com sucesso')

      for widget in direita.winfo_children():
        widget.destroy()

      mostrar()

    except IndexError:
      messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')


  # Logica para mostrar agendamentos
  def mostrar():
    global tree
    global usuario_atual
    id = usuario_atual.get_id()
    lista = agendamento.mostrar_info(id)
    global agendamentos
    agendamentos = []
    for value in lista:
      agendamentos.append(
        agendamento(
          value[0], 
          value[1], 
          value[2],
          value[3],
          value[4]
        )
      )
    
    #Lista para cabeçario
    tabela_header = ['Nº', 'Nome', 'Data', 'Descrição']

    # Criando a Tabela
    tree = ttk.Treeview(direita,
                        height=17,
                        selectmode="extended",
                        columns=tabela_header,
                        show="headings")

    # Vertical scrollbar
    vsb = ttk.Scrollbar(direita, orient="vertical", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')

    direita.grid_rowconfigure(0, weight=12)

    hd = ['nw', 'nw', 'center', 'nw']
    h = [2, 140, 120, 280]
    n = 0

    for col in tabela_header:
      tree.heading(col, text=col.title(), anchor=CENTER)
      # adjust the column's width to the header string
      tree.column(col, width=h[n], anchor=hd[n])

      n += 1
    for i,item in enumerate(agendamentos, start = 1):
      tree.insert('', 'end', values=[i,item.get_nome(),item.get_data(),item.get_des()])
  
  # Criação dos botões
  bt_voltar = Button(janelaAgenda,
                     bd=0,
                     image=img_botaovoltar,
                     command=lambda: [janelaAgenda.destroy(),
                                      tela_inicial()])
  bt_voltar.place(width=150, height=50, x=760, y=13)

  bt_inserir = Button(janelaAgenda,
                      bd=0,
                      image=img_botaoinserir,
                      command=inserir)
  bt_inserir.place(width=80, height=25, x=5, y=398)

  bt_atualizar = Button(janelaAgenda,
                        bd=0,
                        image=img_botaoatualizar,
                        command=atualizar)
  bt_atualizar.place(width=80, height=25, x=100, y=398)

  bt_deletar = Button(janelaAgenda,
                      bd=0,
                      image=img_botaodeletar,
                      command=deletar)
  bt_deletar.place(width=80, height=25, x=195, y=398)
  # Chamando a função mostrar
  mostrar()
  janelaAgenda.mainloop()


# Logica para validar login
def login_valido(username, senha):
  global usuario_atual
  if username and senha:
    if usuario.get_senha(username) != senha:
      return False
    else:
      user = usuario.get_usuario(username)
      usuario_atual = usuario(user[0][1], user[0][2], user[0][3])
      return True
  else:
    return False

    
debug:bool or int = 1 
if debug:
  # with conexao:
  #   i = ["adm", "adm", "adm"]
  #   cur = conexao.cursor()
  #   query = "INSERT INTO usuario (nome, senha, backup) VALUES (?, ?, ?)"
  #   cur.execute(query, i)
  with conexao:
    cur = conexao.cursor()
    query = f"SELECT * FROM usuario"
    cur.execute(query)
    lista = cur.fetchall()
  print(*lista,sep="\n")
  with conexao:
    cur = conexao.cursor()
    query = f"SELECT * FROM agendamento"
    cur.execute(query)
    lista = cur.fetchall()
  print(*lista,sep="\n")

tela_inicial()
