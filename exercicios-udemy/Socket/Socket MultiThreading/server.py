                                    # CRIANDO MULTIPLAS CONEXÕES ENTRE SERVIDOR E CLIENTES

# python .\server.py ---> para executar o servidor ou outro arquivo pelo terminal com python, depois de inserido o caminho a maneira de se executar é essa.





import threading # para fazer uma função rodar do lado da outra (ao mesmo tempo).
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777)) # ligando o servidor.
        server.listen() # significa que o servidor está pronto para receber as conexões. caso não recebe um número específico irá receber quantas conexões aguentar.
    except:
        return print('\nNão foi possível iniciar o servidor.\n') # caso haja algum erro, será encerrada a conexão.

    while True:  # caso não encerre anteriormente.
        client, ender = server.accept() # para o servidor aceitar a conexão do usuário.
        clients.append(client) # adicionando um cliente dentro da lista dos clientes.

        # Iniciando a Thread (feito por último)
        thread = threading.Thread(target=tratamento_de_msg, args=[client])
        thread.start()


def tratamento_de_msg(client):
    while True:
        try:
            msg = client.recv(2048) # quantidade de bytes a serem recebidos.
            broadcast(msg, client)
        except: # caso não seja possível receber a msg do cliente, quer dizer que não está mais conectado. então deve-se apagá-lo.
            deleteClient(client)
            break # para para de ouvir a msg do cliente, uma vez que não está mais conectado.


def broadcast(msg, client): # função para enviar mensagem para todos conectados no servidor, menos para quem enviou a mensagem.
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg) # vai enviar a msg caso seja diferente de quem enviou.
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)


main()
