# JSON > JavaScript object Notation


# JSON              PYTHON

# object            dict
# array             list
# string            str
# number(int)       int
# number(real)      float
# true              TRUE
# false             FAlSE
# null              None

# STRING JSON PARA DICIONÁRIO

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

'''import json

# "json.loads" siginifica: carregar string
dados = json.loads(string_cadastro)
# print(dados)'''

# acessando a chave do dicionário:

'''for dado in dados['dados']:
    print(dado['altura'])
    print((dado['idade']))'''

# ------------------------------------------

# Excluindo a idade da variavel dados:

'''for dado in dados['dados']:
    del dado['idade']
print(dados)
'''

#-----------------------------------------------------------------------------------------------------------------------

                                    #Dicionário para string JSON
                                    #Convertendo para JSON novamente

import json
dados = json.loads(string_cadastro)

#print(dados['dados'][1]) # Acessando por indice.

#"dumps" converte a variável dados para JSON novamente
# "indent" dá uma identação (espaço) para as linhas.
# "sort_keys=True" ordena em ordem alfabética.
json_string = json.dumps(dados, indent=2, sort_keys=True)
print(json_string)

