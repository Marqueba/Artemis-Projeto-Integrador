# Importando bibliotecas responsáveis por envio de emails
import smtplib
import email.message

def enviar_email(email_user, nome, senha):  
    
    corpo_email = """ <p>Olá {}!!!</p> 
                      <p>Sua senha é {}</p>""".format(nome, senha)

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


# In[ ]:
