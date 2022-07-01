# DELETE
import requests
'''url = 'https://reqres.in'
endpoint = '/api/users/2'
requisicao = url + endpoint
print(requisicao)
resposta = requests.request('DELETE', requisicao)
#receberemos o código <Response [204]> significa que não encontrado a requesição, ou seja foi apagado com sucesso.
print(resposta)'''

#----------------------------------------------------------------------

#MANEIRA 2:
requisicao = requests.delete('https://reqres.in/api/users/2')
resposta = requisicao
print(resposta)
