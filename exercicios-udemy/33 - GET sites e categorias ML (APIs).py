#GET - Mercado Livre

import requests

#HTTP GET
# GET: vai consultar ou selecionar dados

'''URL = 'https://api.mercadolibre.com'

endpoint = '/sites'

requisicao = URL + endpoint
print(requisicao)

sites = requests.request('GET', requisicao)
print(sites)
# Acessando as siglas de varios países da "api" do mercado livre.
print(sites.json())

resposta = sites.json()

#Acessando por dicionario:
for resp in resposta:
    print(resp['name'])
'''

#_______________________________________________________________________________________________________________________

## CONSULTANDO CATEGORIAS:

URL = ' https://api.mercadolibre.com'

endpoint = '/sites/MLB/categories'

requisicao = URL + endpoint
print(requisicao)

categorias = requests.request('GET', requisicao)
print(categorias)
# Acessando as siglas de varios países da "api" do mercado livre.
print(categorias.json())

resposta = categorias.json()

#acessando a categoria "name":
for categoria in resposta:
    print(categoria['name'])

print('-' * 50)

for ind, categoria in enumerate(resposta):
    print(f'{ind+1} {categoria["name"]}')

#-----------------------------------------------------------------------------------------------------------------------

#Acessando categoria:
#Modo 2
requisicao = requests.get('https://api.mercadolibre.com/sites/MLB/categories')
print(requisicao)
print(requisicao.json())

resposta = requisicao.json()

for ind, resp in enumerate(resposta):
    print(ind, resp['name'])





