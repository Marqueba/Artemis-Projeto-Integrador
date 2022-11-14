import re
import string
from tkinter import messagebox

class TamanhoSenhaError(Exception):
  pass


class naoContemCaractereMaiusculoError(Exception):
  pass

  
class naoContemCaractereMinusculoError(Exception):
  pass

  
class naoContemCaractereEspecialError(Exception):
  pass

  
class naoContemNumeroError(Exception):
  pass


def senhaForte(senha:str):
  """
  Conterá pelo menos um caractere no intervalo A-Z
  Conterá pelo menos um caractere no intervalo a-z
  Conterá pelo menos um caractere no intervalo 0-9
  Conterá pelo menos um caractere especial
  """
  def contemCaractereMaiusculo(senha:str) -> bool:
    if re.findall("[A-Z]",senha):
      return True
    return False
  def contemCaractereMinusculo(senha:str) -> bool:
    if re.findall("[a-z]",senha):
      return True
    return False
  def contemCaractereEspecial(senha:str) -> bool:
    l = string.punctuation
    for x in senha:
      if x in l:
        return True
    return False
  def contemNumero(senha:str) -> bool:
    if re.findall("[0-9]",senha):
      return True
    return False
  try:
    if not (8 <= len(senha) <= 20):
      raise TamanhoSenhaError
    elif not contemCaractereMaiusculo(senha):
      raise naoContemCaractereMaiusculoError
    elif not contemCaractereMinusculo(senha):
      raise naoContemCaractereMinusculoError
    elif not contemCaractereEspecial(senha):
      raise naoContemCaractereEspecialError
    elif not contemNumero(senha):
      raise naoContemNumeroError
    else:
      return True
  except TamanhoSenhaError:
    messagebox.showerror(title='ATENÇÃO!', message='Tamanho mínimo da Senha é 8 caracteres e máximo é 20.')

    return False
  except naoContemCaractereMaiusculoError:
    messagebox.showerror(title='ATENÇÃO!', message='Senha fraca - deve conter pelo menos uma letra maiuscula')
    return False
  except naoContemCaractereMinusculoError:
    messagebox.showerror(title='ATENÇÃO!', message='Senha fraca - deve conter pelo menos uma letra minuscula')
    return False
  except naoContemCaractereEspecialError:
    messagebox.showerror(title='ATENÇÃO!', message='Senha fraca - deve conter pelo menos um caractere especial')
    return False
  except naoContemNumeroError:
    messagebox.showerror(title='ATENÇÃO!', message='Senha fraca - deve conter pelo menos um número')
    return False

if __name__ == "__main__":
  testes = ["A1!aaaa","A1!aaaaa","A1!aaaaaaaaaaaaaaaaa","A1!aaaaaaaaaaaaaaaaaa"]
  for teste in testes:
    print(f"{len(teste):>5}",teste,"é uma senha valida" if senhaForte(teste) else "não é uma senha valida" )