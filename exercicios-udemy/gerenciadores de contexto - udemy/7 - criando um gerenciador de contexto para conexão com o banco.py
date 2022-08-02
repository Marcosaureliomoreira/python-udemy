# Exemplo Prático
# Gerenciador de contexto para Banco de Dados:

from contextlib import contextmanager
import sqlite3

@contextmanager
def abrir_banco(banco):
    try:
        conexao = sqlite3.connect(banco)
        yield conexao
    finally:
        conexao.commit()
        conexao.close()


with abrir_banco(':memory:') as conexao:
    c = conexao.cursor()
    c.execute("CREATE TABLE pessoas (nome text, email text)")
    c.execute("INSERT INTO pessoas VALUES ('martha', 'maria@email.com')")
    c.execute('SELECT * FROM pessoas')
    print(c.fetchall())

