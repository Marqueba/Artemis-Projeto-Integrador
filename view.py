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

  def get_local(username):
    backup_local = acessar_bd('backup', 'usuario', 'nome', username)
    if backup_local:
      return backup_local[0][0]

  def get_usuario(username):
    user = acessar_bd('*', 'usuario', 'nome', username)
    return user

  def get_id(self):
    id_user = acessar_bd('id', 'usuario', 'nome', self.__nome)
    return id_user[0][0]

  def nome_disponivel(username):
    user = acessar_bd('nome', 'usuario', 'nome', username)
    return False if user else True

  def cadastro_user(nome, senha, backup):
    if nome and senha and backup:
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
      elif not (3 < len(senha) < 20):
        messagebox.showwarning(
          title='ATENÇÃO!',
          message=
          'Tamanho mínimo da Senha é 3 caracteres e máximo de 20 caracteres')
        return False
      elif not (5 < len(backup) < 20):
        messagebox.showwarning(
          title='ATENÇÃO!',
          message=
          'Tamanho mínimo do local é 5 caracteres e máximo de 20 caracteres')
        return False
      else:
        with conexao:
          i = [nome, senha, backup]
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

  def __init__(self, nome, data, des, id_user):
    self.__id = id
    self.__nome = nome
    self.__data = data
    self.__descricao = des
    self.__id_user = id_user

  def inserir_info(i):
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
  def atualizar_info(i):
    with conexao:
      cur = conexao.cursor()
      query = "UPDATE agendamento SET nome=?, dia_agendamento=?, descricao=? WHERE id=?"
      cur.execute(query, i)

  # Deletar Informações
  def deletar_info(i):
    with conexao:
      cur = conexao.cursor()
      query = "DELETE FROM agendamento WHERE id=?"
      cur.execute(query, i)
