# Erros de cadastro
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


# Erros de agendamento
class NenhumAgendamentoSelecionadoError(Exception):
  pass


class NomeAgendamentoVazioError(Exception):
  pass


class DataAgendamentoVaziaError(Exception):
  pass


  
