
import socket

# Código Original

host = 'localhost' # pode ser "localhost" ou o ip da máquina que estou trabalhando
port = 50000 # a porta tem que ser a mesma do servidor para haver a conexão.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conectando ao servidor:
s.connect((host, port))
# para enviar dados para o servidor utilizaos o método "sendall() + a mensagem":

dados = str(input('Digite a mensagem: '))
s.sendall(str.encode(dados)) # o método "str.encode()" garante que a mensagem vai chegar exatamente como deve ser e não vai dar nenhum erro.
data = s.recv(1024) # dados recebidos pelo servidor.
print('Mensagem ecoada: ', data.decode()) # o método "decode()" vai decodificar a mensagem e garantir que consiga ler sem problemas.

# -------------------------------------------------------------------------------------------------------------------------------------------

# ALGORITMO PARA COPIAR A IMAGEM PARA DO SERVIDOR
# Código Secundário

'''host = 'localhost' # pode ser "localhost" ou o ip da máquina que estou trabalhando
port = 50000 # a porta tem que ser a mesma do servidor para haver a conexão.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# conectando ao servidor:
s.connect((host, port))
# para enviar dados para o servidor utilizaos o método "sendall() + a mensagem":

dados = str(input('Arquivo: '))
s.sendall(str.encode(dados)) # o método "str.encode()" garante que a mensagem vai chegar exatamente como deve ser e não vai dar nenhum erro.
with open(dados, 'wb') as file:
    while True:
        data = s.recv(1024) # dados recebidos pelo servidor.
        if not data:
            break
        file.write(data)

print(f'{dados} recebido') # o método "decode()" vai decodificar a mensagem e garantir que consiga ler sem problemas.
'''
