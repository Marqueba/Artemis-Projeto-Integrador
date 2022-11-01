# Importando SQLite
import sqlite3 as lite

#  CRUD
# Create = criar/ Inserir
# Read = Acessar/ Visualizar
# Update = Atualizar
# Delete =  Deletar / Apagar

# Criando conexão
conexao = lite.connect('Bancodedados.db')

class Usuario:
    def __init__(self, id, nome, senha, backup):
        self.__id = id
        self.__nome = nome
        self.__senha = senha
        self.__backup = backup
    
    def realizar_cadastro():
        pass

    def efetuar_login():
        pass

    def efetuar_logout():
        pass

    def consultar_dados():
        pass
    
