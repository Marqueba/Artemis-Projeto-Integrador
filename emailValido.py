from tkinter import messagebox
import re 


teste1 = re.compile(r'^[a-z0-9_.]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')

teste2 = '^[a-z0-9]+[.]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
   

def verificarEmail(email:str) -> bool:
  """
  Criar uma logica para apenas aceitar e-mails validos no padrão:
  nome@dominio
  nome: pode conter letras maiúsculas e minúsculas e números
  domínio: apenas letras e "."
  """
  if not teste1.match(email):  
    if not re.search(teste2,email):
      messagebox.showerror(title='ATENÇÃO!', message='Email invalido.')
      return False
  return True
      
if __name__ == "__main__":
  testes = [
    "email",
    "email@email",
    "Email@email.com",
    "email@email.com.br",
    "email.email@email.com",
    "email.email@email.com.br"
  ]
  for teste in testes:
    print(teste,"é um email valido" if verificarEmail(teste) else "não é um email valido")
