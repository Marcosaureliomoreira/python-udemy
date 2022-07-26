import mysql.connector

# PARTE 1: CRAINDO UM BANCO DE DADOS

'''banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aurelio20"
)

# verificando se esta conectado ao banco.
#print(banco)

cursor = banco.cursor()

#criando banco de dados:
cursor.execute('create database python_youtube')'''
#se não der erro nenhum, o banco foi criado.

#_______________________________________________________________________________________________________________________

#PARTE 2: CRIANDO UMA TABELA

'''banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aurelio20",
    database="python_youtube"
)

# verificando se esta conectado ao banco.
#print(banco)

cursor = banco.cursor()

#criando Tabela no banco de dados python-youtube:
cursor.execute('CREATE TABLE pessoas(nome VARCHAR(255), idade INT(3), email VARCHAR(255))')'''


#_______________________________________________________________________________________________________________________

#PARTE 3: INSERINDO DADOS NA TABELA

'''banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aurelio20',
    database='python_youtube'
)

cursor = banco.cursor()

#MANEIRA 1:
# "%s" significa que os dados serão passados depois/abaixo, em dados.
comando_SQL = 'INSERT INTO pessoas (nome, idade, email) values (%s,%s,%s)'
dados = ('Maria', '40', 'Maria@gamil.com')
cursor.execute(comando_SQL, dados)

banco.commit()'''



#MANEIRA 2 (Minha maneira):

'''comando_SQL = "INSERT INTO pessoas VALUES ('Pedro', '40', 'pedro@gmail.com')"
cursor.execute(comando_SQL)
banco.commit()
'''
#_______________________________________________________________________________________________________________________

# PARTE 4 - Lendo os Dados/Consulta:

'''banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aurelio20',
    database='python_youtube'
)

cursor = banco.cursor()

comando_sql = "SELECT * FROM pessoas"
cursor.execute(comando_sql)
valores_lidos = cursor.fetchall()
#Vai retornar uma lista de tuplas com os dados contidos na tabela.
print(valores_lidos)


#Filtrando valores específicos:
comando_sql = "SELECT nome FROM pessoas WHERE idade = '40'"
cursor.execute(comando_sql)
valores_lidos = cursor.fetchall()
print(valores_lidos)

comando_sql = "SELECT nome, email, idade FROM pessoas WHERE idade > '50'"
cursor.execute(comando_sql)
valores_lidos = cursor.fetchall()'''
#Vai retornar uma lista de tuplas com os dados contidos na tabela.
#print(valores_lidos)

#_______________________________________________________________________________________________________________________

#PARTE 5: Deletando Registros

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aurelio20',
    database='python_youtube'
)

cursor = banco.cursor()

comando_sql = "DELETE FROM pessoas WHERE idade = 65"
cursor.execute(comando_sql)
banco.commit()


# CONFERINDO OS DADOS APÓS A EXCLUSÃO PARA VERIFICAR.
comando_sql = "SELECT * FROM pessoas"
cursor.execute(comando_sql)
dados_lidos = cursor.fetchall()
print(dados_lidos)
