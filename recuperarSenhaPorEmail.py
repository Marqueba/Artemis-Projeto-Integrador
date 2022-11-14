# Importando bibliotecas responsáveis por envio de emails
import smtplib
import email.message

# Importando ramdom e string
import random
import string

from tkinter import messagebox

# Importando requests
import requests
from requests.exceptions import ConnectionError

def enviar_email(email_user:str, nome:str) -> bool:  
    global code

    if not check_internet():
      messagebox.showerror(title = 'ERRO', message = 'Você não está conectado com a Internet!')
      return False
    else:
      size=5
      chars=string.ascii_uppercase + string.digits
      code = ''.join(random.choice(chars) for _ in range(size))

  
      corpo_email = """ <p>Olá {}!!!</p> 
                      <p>Seu código de verificação é {}</p>""".format(nome, code)

      msg = email.message.Message()
      msg['Subject'] = "Recuperação de Senha"
      msg['From'] = 'ifro.suporteartemis@gmail.com'
      msg['To'] = '{}'.format(email_user)
      password = 'uavnkuogzdbovfjh' 
      msg.add_header('Content-Type', 'text/html')
      msg.set_payload(corpo_email )

      s = smtplib.SMTP('smtp.gmail.com: 587')
      s.starttls()
      # Login Credentials for sending the mail
      s.login(msg['From'], password)
      s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
      
def check_internet():
    ''' checar conexão de internet '''
    url = 'https://www.google.com'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        return True
    except ConnectionError:
        return False

# In[ ]:
