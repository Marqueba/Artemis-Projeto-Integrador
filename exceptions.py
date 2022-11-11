class UsuarioSenhaVazio(Exception):
  pass
  messagebox.showerror(title='ERRO', message='Usuário e/ou senha não podem ser vazios' )


class excecaoLocalNascimentoErrado(Exception):
  pass
  messagebox.showerror(title='ERRO',message='O local de nascimento está errado!')


class excecaoNomeIndisponivel(Exception):
  pass
  messagebox.showwarning(title='ATENÇÃO', message='Este nome não está disponível!')


class excecaoTamanhoNome(Exception):
  pass
  messagebox.showwarning(title='ATENÇÃO!',message='Tamanho MÁXIMO do nome 100 caracteres, e no MÍNIMO 5 caracteres')


class excecaoTamanhoSenha(Exception):
  pass
  messagebox.showwarning(title='ATENÇÃO!',message='Tamanho mínimo da Senha 3 caracteres')


class excecaoNenhumAgendamentoSelecionado(Exception):
  pass
  messagebox.showerror(title='ERRO',message='Nenhum agendamento selecionado!')


class excecaoNomeAgendamentoVazio(Exception):
  pass
  messagebox.showerror(title='ERRO', message='O nome do agendamento não pode ser vazio!')


class excecaoDataAgendamentoVazia(Exception):
  pass
  messagebox.showerror(title='ERRO', message='A data não pode ser vazia!')


class excecaoSenhaForte(Exception):
  pass
  

