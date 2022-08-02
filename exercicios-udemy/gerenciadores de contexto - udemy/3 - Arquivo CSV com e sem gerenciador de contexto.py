                                                        # GERENCIADORES DE CONTEXTO

# Escrevendo Arquivo de CSV SEM gerenciador de contexto:
# Nesse formato temos que colocar obrigatoriamente o "close()" no final do arquivo para fechar

import csv
import pandas as pd

arquivo_csv = open('arquivos/exemplo.csv', 'w')
csv_writer = csv.writer(arquivo_csv)
csv_writer.writerow(['Nome', 'Idade', 'Sexo'])
csv_writer.writerow(['Ana', 19, 'Feminino'])
csv_writer.writerow(['Pedro', 23, 'Masculino'])
csv_writer.writerow(['Maria', 21, 'Feminino'])
arquivo_csv.close()
print(arquivo_csv.closed)

# Lendo arquivos pandas:
meu_arquivo = pd.read_csv('arquivos/exemplo.csv')
print(meu_arquivo)



# Escrevendo Arquivo CSV COM gerenciador de contexto:
# Nesse formato o arquivo é fechado automaticamente:

with open('arquivos/exemplo.csv', 'w') as arquivo_csv:
    csv_writer = csv.writer(arquivo_csv)
    csv_writer.writerow(['Nome', 'Idade', 'Sexo'])
    csv_writer.writerow(['Ana', 19, 'Feminino'])
    csv_writer.writerow(['Pedro', 23, 'Masculino'])
    csv_writer.writerow(['Maria', 21, 'Feminino'])