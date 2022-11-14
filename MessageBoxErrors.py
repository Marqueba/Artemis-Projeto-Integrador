"""
Exemplo apenas, os tratamentos de erros que vamos ter: 

===== Tela Login =====

- Nome de usuário ou Senha Incorretos!!! ok


===== Tela Cadastro =====

- Nome de usuário já existe ok
- Tamanho máximo do nome 100, mínimo 5 caracteres ok
- Tamanho mínimo da Senha 3 caracteres ok

===== Tela Ajuda =====

- Local de nascimento errado ok

===== Tela Agendamentos =====

- Nenhum agendamento selecionado ok
- Nome do agendamento não pode ser vazio ok
- Data não pode ser vazia ok

###### Exemplo apenas ########
 
 if nome =='':
      messagebox.showerror('Erro', 'O nome não pode ser vazio')
 else:
     atualizar_info(lista)
     messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

try: 
  print('hello world')
except IndexError:
"""


#login
messagebox.showerror(title='ERRO', message='Usuário e/ou senha incorretos' )
messagebox.showerror(title='ERRO', message='Usuário e/ou senha não podem ser vazios' )


#ajuda
messagebox.showerror(title='ERRO',message='O local de nascimento está errado!')
messagebox.showerror(title='ERRO', message='Usuário e/ou senha não podem ser vazios' )
 
#cadastro
messagebox.showwarning(title='ATENÇÃO', message='Este nome não está disponível!')
messagebox.showwarning(title='ATENÇÃO!',message='Tamanho MÁXIMO do nome 100 caracteres, e no MÍNIMO 5 caracteres')
messagebox.showwarning(title='ATENÇÃO!',message='Tamanho mínimo da Senha 3 caracteres')
messagebox.showerror(title='ERRO', message='Usuário e/ou senha não podem ser vazios' )

#agendamento
messagebox.showerror(title='ERRO',message='Nenhum agendamento selecionado!')
messagebox.showerror(title='ERRO', message='O nome do agendamento não pode ser vazio!')
messagebox.showerror(title='ERRO', message='A data não pode ser vazia!')
messagebox.showinfo(title='PARABÉNS',message='Agendamento confirmado')

