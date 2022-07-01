# Link para cotação de moedas: https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL
import requests


#x = requests.put('https://www.w3schools.com/python/module_requests.asp')
#print(x.text)

#método "get" pega informações da "API"
'''requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
print(requisicao)
print(requisicao.json())'''
#json() é um dicionário em python
#<Response [403]> significa que tudo esta ok.
#404 not found: significa que deu ERRO.
#-----------------------------------------------------------------------------------------------------------------------

'''
#Lendo informaçãoes do meu banco de dados Firebase.
#Método GET - Pegar informações
requisicao = requests.get('https://teste-40f9a-default-rtdb.firebaseio.com/.json')
print(requisicao)
print(requisicao.json())
#_______________________________________________________________________________________________________________________

#Criar informações - POST
#".json" no final do link é uma obrigação do "firebase".
informacoes = '{"Nome": "Candioto"}'
requisicao = requests.post('https://teste-40f9a-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao)
print(requisicao.json())
#-----------------------------------------------------------------------------------------------------------------------

#Editar/Atualizar informações - PATCH

informacoes = '{"Nome": "Daniel", "Sobrenome": "Candiotto", "Idade": "29"}'
requisicao = requests.patch('https://teste-40f9a-default-rtdb.firebaseio.com/-N56PxZKp-W-_7YQIi9x.json', data=informacoes)
print(requisicao)
print(requisicao.json())

#Deletar informações - DELETE

requisicao = requests.delete('https://teste-40f9a-default-rtdb.firebaseio.com/-N56PxZKp-W-_7YQIi9x.json')
print(requisicao)
print(requisicao.json())
'''













#TREINANDO
import re

'''e = re.compile(r'[0-9]+')
ex = e.findall("{'Idade': 27, 'Nome': 'Marcos'}, {'Idade': 37, 'Nome': 'Valeria'}")'''

'''requisicao = requests.get('https://teste-40f9a-default-rtdb.firebaseio.com/.json')

print(requisicao)
print(requisicao.json())'''


informacoes = '{"Nome": "Julio", "Idade": 40}'
requisicao = requests.post('https://teste-40f9a-default-rtdb.firebaseio.com/.json', data=informacoes)
print(requisicao)
print(requisicao.json())


