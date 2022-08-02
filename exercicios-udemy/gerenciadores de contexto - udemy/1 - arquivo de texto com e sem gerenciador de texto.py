                                                        # GERENCIADORES DE CONTEXTO

# Escrevendo Arquivo de Texto SEM gerenciador de contexto:
# Nesse formato temos que colocar obrigatoriamente o "close()" no final do arquivo para fechar
f = open('arquivos/exemplo.txt', 'w')
f.write('Um texto qualquer')
f.close()


# Escrevendo Arquivo de Texto COM gerenciador de contexto:
# Nesse formato o arquivo é fechado automaticamente:
with open('arquivos/exemplo.txt', 'w') as f:
    f.write('Um texto qualquer')





