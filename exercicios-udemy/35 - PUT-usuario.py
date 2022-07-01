
#PUT
#Alterar/Atualizar

import requests


url = 'https://reqres.in'
endpoint = '/api/users/2'
body = {
    "name": "danilo",
    "job": "instrutor ALTERADO"
}
header = {"Content-Type": "application/json"}
requisicao = url + endpoint
resposta = requests.request('PUT', requisicao, json=body, headers=header)

usuario_atualizado = resposta.json()
print(resposta)
print(usuario_atualizado)
