# Conectando com o Banco de dados:

import sqlite3
conexao = sqlite3.connect(':memory:')
c = conexao.cursor()
c.execute("CREATE TABLE pessoas (nome text, email text)")
c.execute("INSERT INTO pessoas VALUES ('martha', 'maria@email.com')")
c.execute('SELECT * FROM pessoas')
print(c.fetchall())
conexao.commit()# enviando informações para o banco:
conexao.close()# fechando o banco:

c.execute('select * from pessoas')
print(c.fetchall())