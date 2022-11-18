# Importando SQLite
import sqlite3 as lite

# Criando conexão
conexao = lite.connect('Bancodedados.db')

# Criando tabela Usuário
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS usuario( " 
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "nome TEXT,"
                "senha TEXT,"
                "email TEXT)")

# Criando tabela Agendamento
with conexao:
    cur = conexao.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS agendamento( " 
                "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                "nome TEXT,"
                "dia_agendamento DATE,"
                "descricao TEXT,"
                "id_user INTEGER"
                "FOREIGN KEY REFERENCES usuario(id))")