"""
Toda logica baseada na ideologia CRUD

C reate ->  Criar   | Inserir
R ead   ->  Acessar | Visualizar
U pdate ->  Atualizar
D elete ->  Deletar | Apagar
"""

# Importando SQLite
import sqlite3 as lite


# Criando conexão
conexao = lite.connect('Bancodedados.db')


#importando o messagebox do tkinter
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


class EmailIndisponivelError(Exception):
  pass


def acessar_bd(atributos: str, tabela: str, chave: str, chave2: str) -> list:
  with conexao:
    query = f"SELECT {atributos} FROM {tabela} WHERE {chave} == ?"
    cur = conexao.cursor()
    cur.execute(query, [chave2])
    lista: list = cur.fetchall()
    return lista


class usuario:

  def __init__(self: object, 
               nome: str, 
               senha: str, 
               email: str, 
               adm: int = 0):
    self.__nome: str = nome
    self.__senha: str = senha
    self.__email: str = email
    self.__adm: int = adm

  
  def get_senha(nome: str) -> str:
    senha_user = acessar_bd('senha', 'usuario', 'nome', nome)
    if senha_user:
      return senha_user[0][0]

  
  def get_email(nome: str) -> str:
    email = acessar_bd('email', 'usuario', 'nome', nome)
    if email:
      return email[0][0]

  
  def get_usuario(nome: str) -> list:
    user = acessar_bd('*', 'usuario', 'nome', nome)
    return user

  
  def get_id(self: object):
    id_user = acessar_bd('id', 'usuario', 'nome', self.__nome)
    return id_user[0][0]

  
  def nome_disponivel(nome: str) -> bool:
    user = acessar_bd('nome', 'usuario', 'nome', nome)
    return False if user else True

  
  def email_disponivel(email: str) -> bool:
    user = acessar_bd('email', 'usuario', 'email', email)
    return False if user else True

  def alterar_senha(senha, id) -> None:
    i = [senha, id]
    with conexao:
      cur = conexao.cursor()
      query = "UPDATE usuario SET senha=? WHERE id=?"
      cur.execute(query, i)

  def cadastro_user(nome: str, 
                    senha: str, 
                    email: str) -> bool:
    try:
      if nome is None or senha is None or email is None:
        raise UsuarioSenhaEmailVazioError

      elif not (5 < len(nome) < 20):
        raise TamanhoNomeError

      elif not usuario.nome_disponivel(nome):
        raise NomeIndisponivelError

      elif not usuario.email_disponivel(email):
        raise EmailIndisponivelError

      elif not senhaValida.senhaForte(senha):
        raise SenhaFracaError

      elif not emailValido.verificarEmail(email):
        raise EmailInvalidoError

    except UsuarioSenhaEmailVazioError:
      return False

    except TamanhoNomeError:
      messagebox.showerror('ATENÇÃO!',
                           'Tamanho mínimo do Nome é 5 caracteres e máximo de 20 caracteres')
      return False

    except NomeIndisponivelError:
      messagebox.showerror('ATENÇÃO', 'Este nome não está disponível!')
      return False

    except SenhaFracaError:
      return False

    except EmailInvalidoError:
      return False

    except EmailIndisponivelError:
      messagebox.showerror('ATENÇÃO', 'Este email não está disponível!')
      return False

    else:
      with conexao:
        i = [nome, senha, email]
        cur = conexao.cursor()
        query = "INSERT INTO usuario (nome, senha, email) VALUES (?, ?, ?)"
        cur.execute(query, i)
      return True


class agendamento:

  def __init__(self: object, 
               id: int or None, 
               nome: str, 
               data: str, 
               des: str, 
               id_user: int):
    self.__id: int = id
    self.__nome: str = nome
    self.__data: str = data
    self.__descricao: str = des
    self.__id_user: int = id_user

  
  def set_id(self: object, 
             id: int) -> None:
    self.__id = id

  
  def get_id(self: object) -> int:
    return self.__id

  
  def get_nome(self: object) -> str:
    return self.__nome

  
  def get_data(self: object) -> str:
    return self.__data

  
  def get_des(self: object) -> str:
    return self.__descricao

  
  def inserir_info(self: object) -> None:
    i = [self.__nome, self.__data, self.__descricao, self.__id_user]
    with conexao:
      cur = conexao.cursor()
      query = "INSERT INTO agendamento (nome, dia_agendamento, descricao,id_user) VALUES (?, ?, ?, ?)"
      cur.execute(query, i)

  
  def mostrar_info(id_user: int) -> list:
    lista = []
    informacao = acessar_bd("*", "agendamento", "id_user", id_user)
    for i in informacao:
      lista.append(i)
    return lista

  
  def atualizar_info(self: object) -> None:
    i = [self.__nome, self.__data, self.__descricao, self.__id_user]
    with conexao:
      cur = conexao.cursor()
      query = "UPDATE agendamento SET nome=?, dia_agendamento=?, descricao=? WHERE id=?"
      cur.execute(query, i)

  
  def deletar_info(self: object) -> None:
    i = str(self.__id)
    with conexao:
      cur = conexao.cursor()
      query = "DELETE FROM agendamento WHERE id=?"
      cur.execute(query, i)
