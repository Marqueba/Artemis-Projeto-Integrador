# Como fazer o tratamento de exceção
### Seguindo o seguinte padrão fazer todos os tratamento de exceção
```
try: 
  if condicaoExcecao:
    raise Error
except Error:
  messagebox.showerror("Erro", "Mensagem de erro")
else:
  #sucesso
  return True
```
### Como criar as caixas de mensagem na tela 
```
from tkinter import messagebox

messagebox.showerror("erro", "Mensagem de erro")
```
### Como criar as exceções personalizadas 

#### Nos vamos seguir o seguinte padrão

- Nome auto descritivo
- Seguido por Error no final
- palavras separadas por letra maiuscula

```
class NomeExcecaoError(Exception):
  pass
```

### Substituir as messageboxs pelos tratamentos de exceção no 'main.py'

- Provavelmente há mais a ser adicionados...
