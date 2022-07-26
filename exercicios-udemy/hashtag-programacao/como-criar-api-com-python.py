#Replit.com
# Código contruido para rodar no "replit"
# Mostrando como se coloca um site no ar.
# OBS: Depois de algum tempo,semanas a API para de funcionar, temos que ir lá e tentar ligar novamente.

import pandas as pd
#from flask import Flask, jsonify

'''#iniciando o flask:
app = Flask(__name__)

#construir as funcionalidades:
@app.route('/') # diz qual link vai rodar a página abaixo. "/" significa que será a página de entrada do site.
def homepage():
  return 'Essa é a homepage do site'

#Página de contatos do site.
@app.route('/contatos')
def contatos():
  return 'Essa é a página de contatos do site'

# Rodar a nossa api:
# para rodar online no replit temos que passar o host 0.0.0.0 e assim ficará acessível por todos.
# como farei abaixo.
app.run(host='0.0.0.0')

#tabela = pd.read_csv('12-18 - Criando API no Python.csv')
#total_vendas = tabela['Vendas'].sum()
#print(total_vendas)'''

#_______________________________________________________________________________________________________________________


# Construção da minha API para ser consumida
# codigo usado no replit.com


#iniciando o flask:
#depois de já instalado.
'''app = Flask(__name__)

#construir as funcionalidades:
@app.route('/') # diz qual link vai rodar a página abaixo. "/" significa que será a página de entrada do site.
def homepage():
  return 'A API está no ar'

#Função para calcular vendas.
@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')
  total_vendas = tabela['Vendas'].sum()
  print(total_vendas)
  resposta = {"total_vendas": total_vendas}
  return jsonify(resposta)

  # "jsonify()" é um métoda para tranformar nosso arquivo em json para ser consumido.

# Rodar a nossa api:
# para rodar online no replit temos que passar o host 0.0.0.0 e assim ficará acessível por todos.
# como farei abaixo.
app.run(host='0.0.0.0')
'''

#_______________________________________________________________________________________________________________________

# Consumindo minha própria API:

import requests

link = 'https://minhaapi.marcosdores.repl.co/pegarvendas'

requesicao = requests.get('https://minhaapi.marcosdores.repl.co/mediavendas')
print(requesicao)
print(requesicao.json())

dicionario = requesicao.json()

print(dicionario)
