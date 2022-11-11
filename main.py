"""

Protejo Integrador Ártemis

É o projeto integrador desenvolvido por alunos do 2° ano de informática vespertino
do Instituto Federal de Educação, Ciência e Tecnologia de Rondônia Campus Porto Velho
Calama para obtenção de notas nas disciplinas de Banco de Dados, Fundamentos de Análises 
de Sistemas, Linguagem de Programação e Programação Orientada a Objetos. O objetivo 
deste projeto é desenvolver as habilidades trabalhadas em cada uma dessas disciplinas 
criando um planner que auxilie na organização de discentes e docentes.

Integrantes:

- Marcos Reis Dutra
- João Pedro Monteiro Ferreira
- Nicolle Cristini Dias
- Isabella Cristina Queiroz

"""


#importando biblioteca do sistema
import os


# Importando Banco de dados
import banco

# Importando as classes a serem utilizadas
from view import usuario, agendamento


# Importando o sqlite3
import sqlite3 as lite


# Importando o Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Importando tkcalendar
from tkcalendar import Calendar
from tkcalendar import DateEntry


# Declaração de variaveis globais
conexao = lite.connect('Bancodedados.db')
global usuario_atual
global tree

# Caso o banco de dados não existe ele será criado
if not os.path.isfile("Bancodedados.db"):
  os.system('python banco.py')


def tela(nome="Planner Ártemis"):
  tela = Tk()
  tela.title(nome)
  tela.geometry("900x450+610+153")
  tela.resizable(width=False, height=False)
  return tela


# Criando janela
def tela_inicial():
  janelaInicial = tela()
  
  img_telainicial = PhotoImage(file='images/fundos/TelaInicial.png')
  img_botaologin = PhotoImage(file='images/botoes/BotaoLogin.png')
  img_botaocadastro = PhotoImage(file='images/botoes/BotaoCadastro.png')
  img_botaosobre = PhotoImage(file='images/botoes/BotaoSobre.png')

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
  janelaSobre = tela('Planner Ártemis - Sobre')

  img_telasobre = PhotoImage(file='images/fundos/TelaSobre.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')

  lab_fundo = Label(janelaSobre, image=img_telasobre)
  lab_fundo.pack()

  # Criação dos botões
  bt_voltar = Button(janelaSobre, bd=0, image=img_botaovoltar, command=lambda: [janelaSobre.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  janelaSobre.mainloop()


def tela_login():
  janelaLogin = tela('Planner Ártemis - Login')

  img_telalogin = PhotoImage(file='images/fundos/TelaLogin.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoinicia = PhotoImage(file='images/botoes/BotaoIniciarsessao.png')
  img_btesquece = PhotoImage(file='images/botoes/BotaoEsquece.png')
  img_botaocadastro = PhotoImage(file='images/botoes/BotaoRcadastro.png')
  
  lab_fundo = Label(janelaLogin, image=img_telalogin)
  lab_fundo.pack()

  # Configurando entrada de dados
  esconda_senha = StringVar()

  en_username = Entry(janelaLogin, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  en_senha = Entry(janelaLogin, textvariable=esconda_senha, show='*', bd=2, font=("Calibri", 15), justify=CENTER)
  en_senha.place(width=392, height=44, x=253, y=235)

  ########## Criação dos botões
  bt_voltar = Button(janelaLogin, bd=0, image=img_botaovoltar, command=lambda: [janelaLogin.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)
  
  bt_cadastro = Button(janelaLogin, bd=0, image=img_botaocadastro, command=lambda: [janelaLogin.destroy(), tela_cadastro()])
  bt_cadastro.place(width=130, height=30, x=517, y=298)

  # Botão Iniciar Sessão
  bt_iniciasessao = Button(janelaLogin, bd=0, image=img_botaoinicia, command=lambda: [])

  bt_iniciasessao.place(width=150, height=50, x=698, y=365)

  # Botão Esqueceu senha?
  bt_esquecesenha = Button(janelaLogin, bd=0, image=img_btesquece, command=lambda: [janelaLogin.destroy(), tela_ajuda()])
  bt_esquecesenha.place(width=130, height=30, x=252, y=298)

  janelaLogin.mainloop()


def tela_cadastro():
  janelaCadastro = tela('Planner Ártemis - Cadastro')

  img_telacadastro = PhotoImage(file='images/fundos/Telacadastro.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoconcluir = PhotoImage(file='images/botoes/BotaoConcluir.png')
  

  lab_fundo = Label(janelaCadastro, image=img_telacadastro)
  lab_fundo.pack()

  # Configurando entrada de dados

  en_username = Entry(janelaCadastro, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  en_senha = Entry(janelaCadastro, textvariable=StringVar(), show='*', bd=2, font=("Calibri", 15), justify=CENTER)
  en_senha.place(width=392, height=44, x=253, y=235)

  en_local = Entry(janelaCadastro, bd=2, font=("Calibri", 15), justify=CENTER)
  en_local.place(width=392, height=44, x=253, y=333)

  def logar_usuario(nome,senha,backup):
    global usuario_atual
    usuario_atual = usuario(nome, senha, backup)

  ########## Criação dos botões
  bt_voltar = Button(janelaCadastro, bd=0, image=img_botaovoltar, command=lambda: [janelaCadastro.destroy(), tela_inicial()])
  bt_voltar.place(width=150, height=50, x=62, y=365)
  

  ########## Criação dos botões
  bt_concluir = Button( janelaCadastro, bd=0, image=img_botaoconcluir, command=lambda: [logar_usuario(en_username.get(), en_senha.get(), en_local.get()),janelaCadastro.destroy(), tela_agendamentos()] if usuario.cadastro_user(en_username.get(), en_senha.get(), en_local.get()) else [])
  bt_concluir.place(width=150, height=50, x=698, y=365)

  janelaCadastro.mainloop()


def tela_ajuda():
  janelaAjuda = tela('Planner Ártemis - Ajuda')

  img_telaajuda = PhotoImage(file='images/fundos/TelaAjuda.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaorecupera = PhotoImage(file='images/botoes/BotaoRecuperarsenha.png')

  lab_fundo = Label(janelaAjuda, image=img_telaajuda)
  lab_fundo.pack()

  # Configurando entrada de dados
  en_username = Entry(janelaAjuda, bd=2, font=("Calibri", 15), justify=CENTER)
  en_username.place(width=392, height=44, x=253, y=137)

  en_local = Entry(janelaAjuda, bd=2, font=("Calibri", 15), justify=CENTER)
  en_local.place(width=392, height=44, x=253, y=235)

  # Criação dos botões
  bt_voltar = Button(janelaAjuda, bd=0, image=img_botaovoltar, command=lambda: [janelaAjuda.destroy(), tela_login()])
  bt_voltar.place(width=150, height=50, x=62, y=365)

  bt_recuperar = Button(janelaAjuda, bd=0, image=img_botaorecupera, command=lambda: [ ])
  bt_recuperar.place(width=200, height=50, x=350, y=341)

  
  janelaAjuda.mainloop()


def tela_agendamentos():
  janelaAgenda = tela('Planner Ártemis - Agendamentos')

  img_cima = PhotoImage(file='images/fundos/cima.png')
  img_lado = PhotoImage(file='images/fundos/lado.png')
  img_botaovoltar = PhotoImage(file='images/botoes/BotaoVoltar.png')
  img_botaoinserir = PhotoImage(file='images/botoes/BotaoInserir.png')
  img_botaoatualizar = PhotoImage(file='images/botoes/BotaoAtualizar.png')
  img_botaodeletar = PhotoImage(file='images/botoes/BotaoDeletar.png')
  img_botaoconfirma = PhotoImage(file='images/botoes/BotaoConfirmar.png')

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
