from tkinter import messagebox
import re 
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
      
def VerificarEmail(email:str) -> bool:
  """
  Criar uma logica para apenas aceitar e-mails validos no padrão:
  nome@dominio
  nome: pode conter letras maiúsculas e minúsculas e números
  domínio: apenas letras e "."
  """
  if not re.search(regex,email):  
    messagebox.showerror(title='ATENÇÃO!', message='Email invalido.')
    return False
  return True
      
  
