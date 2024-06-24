

import socket

# Códgo original

host = 'localhost'
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET -> indica que estou trabalhando com IPV4.
# SOCK_STREAM -> indica que estou trabalhando com o protocolo TCP.
s.bind((host, port))
# o método "bind" recebe apenas um único parâmetro, por isso o parêntese duplo.
s.listen()
# "listen" é o modo de escuta, acima a variáel "s" está sendo colocada em modo de escuta.
print('Aguardado conexão de um cliente...')
conn, ender = s.accept()
# "conn" e "ender" -> significa conexão e endereço respectivamente, variáveis usadas para aceitar a conexão. serão o retorno do método accept.

print('Conectado em', ender) # para sabe em qual porta está conectado.

# troca mensagens:
while True:
    caracteres = []
    data = conn.recv(1024) # a variável "data" vai receber a conexão da variável "conn" através do método "recv()" até quantidade de dados especificada.
    if not data: # quando não tiver mas dados a receber, a conexão será fechada.
        print('Fechando a conexão')
        conn.close() # Fechando conexão
        break # saindo do laço "while"
    conn.sendall(data) # se tiver dados, será enviados de volta para o cliente. método "sendall()" envia tudo.


# ----------------------------------------------------------------------------------------------------------------------------


# Código secundário

'''host = 'localhost'
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET -> indica que estou trabalhando com IPV4.
# SOCK_STREAM -> indica que estou trabalhando com o protocolo TCP.
s.bind((host, port))
# o método "bind" recebe apenas um único parâmetro, por isso o parêntese duplo.
s.listen()
# "listen" é o modo de escuta, acima a variáel "s" está sendo colocada em modo de escuta.
print('Aguardado conexão de um cliente...')
conn, ender = s.accept()
# "conn" e "ender" -> significa conexão e endereço respectivamente, variáveis usadas para aceitar a conexão. serão o retorno do método accept.

print('Conectado em', ender) # para sabe em qual porta está conectado.

namefile = conn.recv(1024).decode()


with open(namefile, 'wb') as file:
    for data in file.readlines():
        conn.send(data)
    print('Arquivo enviado!')'''

