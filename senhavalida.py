import re
import string


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
    #print("TamanhoSenhaError")
    return False
  except naoContemCaractereMaiusculoError:
    #print("naoContemCaractereMaiusculoError")
    return False
  except naoContemCaractereMinusculoError:
    #print("naoContemCaractereMinusculoError")
    return False
  except naoContemCaractereEspecialError:
    #print("naoContemCaractereEspecialError")
    return False
  except naoContemNumeroError:
    #print("naoContemNumeroError")
    return False

testes = ["A1!aaaa","A1!aaaaa","A1!aaaaaaaaaaaaaaaaa","A1!aaaaaaaaaaaaaaaaaa"]
for teste in testes:
  print(f"{len(teste):>5}",teste,"é uma senha valida" if senhaForte(teste) else "não é uma senha valida" )