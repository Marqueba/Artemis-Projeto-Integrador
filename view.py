# Importando SQLite
import sqlite3 as lite

#  CRUD
# Create = criar/ Inserir
# Read = Acessar/ Visualizar
# Update = Atualizar
# Delete =  Deletar / Apagar

# Criando conexão
conexao = lite.connect('Bancodedados.db')

from tkinter import messagebox


# Importando sistema de validação de senha
import senhaValida


# Importando sistema de validação de e-mail
import emailValido


def acessar_bd(atributos, tabela, chave, chave2):
  with conexao:
    cur = conexao.cursor()
    query = f"SELECT {atributos} FROM {tabela} WHERE {chave} == ?"
    cur.execute(query, [chave2])
    lista = cur.fetchall()
    return lista


class usuario:

  def __init__(self, nome, senha, backup):
    self.__nome = nome
    self.__senha = senha
    self.__backup = backup

  def get_senha(username):
    senha_user = acessar_bd('senha', 'usuario', 'nome', username)
    if senha_user:
      return senha_user[0][0]

  def get_email(username):
    backup_email = acessar_bd('backup', 'usuario', 'nome', username)
    if backup_email:
      return backup_email[0][0]

  def get_usuario(username):
    user = acessar_bd('*', 'usuario', 'nome', username)
    return user

  def get_id(self):
    id_user = acessar_bd('id', 'usuario', 'nome', self.__nome)
    return id_user[0][0]

  def nome_disponivel(username):
    user = acessar_bd('nome', 'usuario', 'nome', username)
    return False if user else True

  def cadastro_user(nome, senha, email):
    if nome and senha and email:
      if not (5 < len(nome) < 20):
        messagebox.showwarning(
          title='ATENÇÃO!',
          message=
          'Tamanho mínimo do Nome é 5 caracteres e máximo de 20 caracteres')
        return False
      elif not usuario.nome_disponivel(nome):
        messagebox.showwarning(title='ATENÇÃO',
                               message='Este nome não está disponível!')
        return False
      elif not senhaValida.senhaForte(senha):
        return False
      elif not emailValido.verificarEmail(email):
        return False
      else:
        with conexao:
          i = [nome, senha, email]
          cur = conexao.cursor()
          query = "INSERT INTO usuario (nome, senha, backup) VALUES (?, ?, ?)"
          cur.execute(query, i)
        return True
    else:
      messagebox.showerror(
        title='ERRO',
        message='Usuário e/ou senha e/ou local não podem ser vazios')
      return False


class agendamento:
  def __init__(self, id:id, nome:str, data:str, des:str, id_user:int):
    self.__id = id
    self.__nome = nome
    self.__data = data
    self.__descricao = des
    self.__id_user = id_user

  
  def set_id(self, id):
    self.__id = id


  def get_id(self):
    return self.__id

    
  def get_nome(self):
    return self.__nome 

    
  def get_data(self):
    return self.__data

    
  def get_des(self):
    return self.__descricao

    
  def inserir_info(self):
    i = [self.__nome, self.__data, self.__descricao, self.__id_user]
    with conexao:
      cur = conexao.cursor()
      query = "INSERT INTO agendamento (nome, dia_agendamento, descricao,id_user) VALUES (?, ?, ?, ?)"
      cur.execute(query, i)

  # Visualizar informações
  def mostrar_info(id_user):
    lista = []
    informacao = acessar_bd("*", "agendamento", "id_user", id_user)
    for i in informacao:
      lista.append(i)
    return lista

  # Atualizar Informações
  def atualizar_info(self):
    i = [self.__nome, self.__data, self.__descricao, self.__id_user]
    with conexao:
      cur = conexao.cursor()
      query = "UPDATE agendamento SET nome=?, dia_agendamento=?, descricao=? WHERE id=?"
      cur.execute(query, i)

  # Deletar Informações
  def deletar_info(self):
    i = str(self.__id)
    with conexao:
      cur = conexao.cursor()
      query = "DELETE FROM agendamento WHERE id=?"
      cur.execute(query, i)
