# Importando bibliotecas responsáveis por envio de emails
import smtplib
import email.message


# Importando dependencias a serem utilizados no modulo 
import random
import string
from tkinter import messagebox


# Importando requests
import requests
from requests.exceptions import ConnectionError


def check_internet() -> bool:
  ''' checar conexão de internet '''
  url = 'https://www.google.com'
  timeout = 5
  try:
    requests.get(url, timeout=timeout)
  except ConnectionError:
    return False
  else:
    return True


def enviar_email(email_user: str, nome: str) -> bool or str:  
  if not check_internet():
    messagebox.showerror(title = 'ERRO', message = 'Você não está conectado com a Internet!')
    return False
  else:
    tamanhoCodigo: int = 5
    caracteres: str = string.ascii_uppercase + string.digits
    
    codigo: str = ''.join(random.choice(caracteres) for _ in range(tamanhoCodigo))
    corpo_email: str = """ <p>Olá {}!!!</p> 
                    <p>Seu código de verificação é {}</p>
                    <p>Caso não tenha sido você, sua conta corre perigo!</p>
                    """.format(nome, codigo)

    msg: object = email.message.Message()
    msg['Subject'] = "Recuperação de Senha"
    msg['From'] = 'ifro.suporteartemis@gmail.com'
    msg['To'] = '{}'.format(email_user)
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    senha: str = 'uavnkuogzdbovfjh' 

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], senha)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    return codigo