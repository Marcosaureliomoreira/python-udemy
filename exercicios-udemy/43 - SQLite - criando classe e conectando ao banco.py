# Criando classe e conectando ao banco

import sqlite3

class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __repr__(self):
        return f'Pessoa (nome: {self.nome}, email: {self.email})'


ana = Pessoa('ana', 'ana@email.com')
pedro = Pessoa('Pedro', 'pedrinho@email.com')
#print(ana)
#print(pedro)

# Criando conexão com o Banco de dados:

conexao = sqlite3.connect('pessoa.db')

#Vai sempre criar um banco de dados e criar novas tabelas, não dará erro, mesmo se já existir.
#conexao = sqlite3.connect(':memory:')

# "cursor" é uma espécie de ponteiro que vai selecionar os dados, inserir, criar consultas etc.
c = conexao.cursor()

# CRUD
#-----
# Create
# Read
# Update
# Delete

# Opções de tipos primitivos do SQLite3: null, integer, real, text, blob
#Criando tabela no banco de dados:

#c.execute("CREATE TABLE pessoas (nome text, email text)")

#Inserindo dados na tabela:
c.execute("INSERT INTO pessoas VALUES ('maria', 'maria@email.com')")
c.execute("INSERT INTO pessoas VALUES ('danilo', 'danilo@email.com')")

#INSERINDO DADOS DA CLASSE "PESSOA" CRIADA ANTERIORMENTE:
# Melhor maneira para inserir dados no caso de "orientação a objetos" para não receber SQL injection.
c.execute("INSERT INTO pessoas VALUES (?, ?)", (pedro.nome, pedro.email))

# Realizando consultas na tabela:
c.execute("SELECT * FROM pessoas")

# "fetchone" pega apenas uma pessoa do banco, para pegar todas se usa o "fetchall"
print(c.fetchall())

# Depois de terminar, no final temos que dar "commit" para enviar as requisições e dar um "close" para fechar o banco.
conexao.commit()
conexao.close()

#_______________________________________________________________________________________________________________________
                                   #Maneira correta de inserir dados no bando

'''# IMPORTANTE:
# Aqui é uma tupla pq possui mais de um dado:
nomes = ('pedro', 'pedro@emeil')
print(type(nomes))

# Aqui é uma str pq possui apema um dado:
nome = ('pedro')
print(type(nome))

# Se for apenas inserir um dado no banco de dados, tem que colocar uma vírgula no final para evitar uma possível "SQL injection" como está abaixo.
nome = ('pedro',)
print(type(nome))'''

