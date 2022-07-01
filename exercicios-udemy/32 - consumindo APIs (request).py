
#Consumindo APIs

#Back End    << API >> Front End
import json

import requests

#HTTP GET
# GET: vai consultar ou selecionar dados

URL = 'https://reqres.in'

endpoint = '/api/users/2'

requisicao = URL + endpoint
print(requisicao)

usuario = requests.request('GET', requisicao)
print(usuario)
# tranformando os dados da api em dicionario.
print(usuario.json())

#variável recebendo o dicionario "usuario" para ser trabalhado
resposta = usuario.json()

#Acessando somente o email, mas antes temos que acessar o primeiro dicionário que é "data".
print(resposta['data']['email'])
print(resposta['data']['avatar'])





#_______________________________________________________________________________________________________________________
# MODO 2:
'''requisicao = requests.get('https://reqres.in/api/users/2')
print(requisicao)
print(requisicao.json())
resp = requisicao.json()
print(resp['data']['first_name'], end=' ')
print(resp['data']['last_name'])
print(resp['data']['email'])
'''
