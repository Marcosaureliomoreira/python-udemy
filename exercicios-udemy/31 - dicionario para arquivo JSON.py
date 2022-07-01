#ESCREVENDO ARQUIVOS JSON

string_cadastro = '''
{
     "dados": [
        {
            "usuario": "ana",
            "idade": 20,
            "altura": 1.59,
            "email": null,
            "ativado": false

        },
        {
            "usuario": "Pedro",
            "idade": 26,
            "altura": 1.81,
            "email": "pedrinho@email.com",
            "ativado": true
        }
    ]
}
'''

import json
dados = json.loads(string_cadastro)

# CRIANDO ARQUIVO JSON:
# "dump" sem o "s" significa que esta passando para um arquivo e não para uma string.
'''with open('novo_json.json', 'w') as arquivo_json: # "arquivo_json" variável temporária.
    json.dump(dados, arquivo_json, indent=2)'''


#-----------------------------------------------------------------------------------------------------------------------

                                    #ARQUIVO JSON PARA DICIONÁRIO

#LENDO ARQUIVO JSON
with open('novo_json.json') as arquivo_json:
    novo_dicionario = json.load(arquivo_json)
    # "load" sem o "s" porque vai carregar um arquivo e não uma string.


print(novo_dicionario)
for dado in novo_dicionario['dados']:
    print(dado['email'])
