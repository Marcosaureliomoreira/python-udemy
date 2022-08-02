                                                        # GERENCIADORES DE CONTEXTO

# Escrevendo Arquivo de JSON SEM gerenciador de contexto:
# Nesse formato temos que colocar obrigatoriamente o "close()" no final do arquivo para fechar
import json

dic_exemplo = {'mensagem': 'Um texto qualquer'}


arquivo_json = open('arquivos/exemplo.json', 'w')
json.dump(dic_exemplo, arquivo_json, indent=2)
arquivo_json.close()


# Escrevendo Arquivo de Texto COM gerenciador de contexto:
# Nesse formato o arquivo é fechado automaticamente:

with open('arquivos/exemplo.json', 'w') as arquivo_json:
    json.dump(dic_exemplo, arquivo_json, indent=2)

