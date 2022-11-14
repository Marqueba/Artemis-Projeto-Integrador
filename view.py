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


#declaração das exceções
class NomeIndisponivelError(Exception):
  pass


class TamanhoNomeError(Exception):
  pass


class UsuarioSenhaEmailVazioError(Exception):
  pass


class SenhaFracaError(Exception):
  pass


class EmailInvalidoError(Exception):
  pass


def acessar_bd(atributos: str, tabela: str, chave: str, chave2: str) -> list:
  with conexao:
    query = f"SELECT {atributos} FROM {tabela} WHERE {chave} == ?"
    cur = conexao.cursor()
    cur.execute(query, [chave2])
    lista: list = cur.fetchall()
    return lista


class usuario:

  def __init__(self: object, nome: str, senha: str, email: str, adm: int = 0):
    self.__nome: str = nome
    self.__senha: str = senha
    self.__email: str = email
    self.__adm: int = adm

  def get_senha(username: str) -> str:
    senha_user = acessar_bd('senha', 'usuario', 'nome', username)
    if senha_user:
      return senha_user[0][0]

  def get_email(username: str) -> str:
    email = acessar_bd('email', 'usuario', 'nome', username)
    if email:
      return email[0][0]

  def get_usuario(username: str) -> list:
    user = acessar_bd('*', 'usuario', 'nome', username)
    return user

  def get_id(self: object):
    id_user = acessar_bd('id', 'usuario', 'nome', self.__nome)
    return id_user[0][0]

  def nome_disponivel(username: str) -> bool:
    user = acessar_bd('nome', 'usuario', 'nome', username)
    return False if user else True

  def cadastro_user(nome: str, senha: str, email: str) -> bool:
    try:
      if nome is None or senha is None or email is None:
        raise UsuarioSenhaEmailVazioError
        
      elif not (5 < len(nome) < 20):
        raise TamanhoNomeError
        
      elif not usuario.nome_disponivel(nome):
        raise NomeIndisponivelError

      elif not senhaValida.senhaForte(senha):
        raise SenhaFracaError
        
      elif not emailValido.verificarEmail(email):
        raise EmailInvalidoError

      """ Criar uma exceção para email disponivel """

    except UsuarioSenhaEmailVazioError:
      return False
    except TamanhoNomeError:
      messagebox.showerror('ATENÇÃO!','Tamanho mínimo do Nome é 5 caracteres e máximo de 20 caracteres')
      return False
    except NomeIndisponivelError:
      messagebox.showerror('ATENÇÃO','Este nome não está disponível!')
      return False
    except SenhaFracaError:
      return False
    except EmailInvalidoError:
      return False
    else:
      with conexao:
        i = [nome, senha, email]
        cur = conexao.cursor()
        query = "INSERT INTO usuario (nome, senha, email) VALUES (?, ?, ?)"
        cur.execute(query, i)
      return True



class agendamento:

  def __init__(self, id: id, nome: str, data: str, des: str, id_user: int):
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
