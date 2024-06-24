import socket
import threading



                                                        # multiplas conexões com o servidor

clientes = []

# FUNÇÃO PRINCIPAL
def treinando_socket():
    host = 'localhost'
    door = 50000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, door))
    s.listen()
    print('aguadando conexão...')
    while True:
        client, ender = s.accept()
        print('Conectado em', ender)
        clientes.append(client)
        print()
        thread = threading.Thread(target=tratando_msg, args=[client])
        thread.start()


def tratando_msg(client):
    while True:
        try:
            msg = client.recv(1024)
            falar_com_todos(msg, client)
            print(msg.decode('utf-8'))
        except:
            delete_client(client)
            client.close()
            print(f'Usuário {msg.decode()}desconectado')
            break


# CRIAR UMA FUNÇÃO PARA ENVIAR MENSAGEM PARA TODOS CONECTADOS AO SERVIDOR, MENOS PARA QUEM JÁ ENVIOU.
def falar_com_todos(msg, client):
    for clientItem in clientes:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                delete_client(clientItem)


def delete_client(client):
    clientes.remove(client)


treinando_socket()










# Conversando com cliente

'''clientes = []

def treinando_socket():
    host = 'localhost'
    door = 50000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, door))
    s.listen()
    print('aguadando conexão...')
    conn, ender = s.accept()
    print('Conectado em', ender)

    while True:
        data = conn.recv(1024)
        print('Cliente' ,ender, ':',  data.decode())
        if not data:
            print('Fechando conexão...')
            conn.close()
            break
        else:
            conn.sendall(data)'''