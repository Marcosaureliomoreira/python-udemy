
#POST
#Inserir / Criar

import requests

'''url = 'https://reqres.in'
endpoint = '/api/users'
body = {
    "name": "danilo",
    "job": "Instrutor"
}
header = {"Content-Type": "application/json"}
requisicao = url + endpoint
resposta = requests.request('POST', requisicao, json=body, headers=header)

#Response = [201] significa que algo foi criado.
#print(resposta)
usuario = resposta.json()
print(usuario)
for indicie, nome in dict(usuario).items():
    print(indicie, nome)
    
#__________________________________________________________________
    
# MANEIRA 2:
body = {
    "name": "danilo",
    "job": "Instrutor"
}
requisicao = requests.post('https://reqres.in/api/users', data=body)
print(requisicao)
print(requisicao.json())
'''
#-----------------------------------------------------------------------------------------------------------------------

#API/Login
#POST LOGIN

url = 'https://reqres.in'
endpoint = '/api/login'
body = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
header = {"Content-Type": "application/json"}
requisicao = url + endpoint
resposta = requests.request('POST', requisicao, json=body, headers=header)

token = resposta.json()
# Aqui vamos receber o "token" de acesso, indicando que o login foi feito com sucesso.
print(token)

#_________________________________________________________________________

#MANEIRA 2:

body = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
requisicao = requests.post('https://reqres.in/api/login', data=body)
tok = requisicao.json()
print(tok)








