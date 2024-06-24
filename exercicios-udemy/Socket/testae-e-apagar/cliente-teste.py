import socket
import threading

# Conversando com o servidor


def treinando_socket_cl():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        host = 'localhost'
        door = 50000
        client.connect((host, door))
    except:
        print('não foi possível conectar-se ao servidor')


    usuario = str(input('Usuário: '))
    print('Conectado')

    thread1 = threading.Thread(target=recebe_msg, args=[client])
    thread2 = threading.Thread(target=enviar_MSG, args=[client, usuario])

    thread1.start()
    thread2.start()


def recebe_msg(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            print('\nNão foi possível permanecer ao servidor\n')
            print('Pressione ENTER para continuar...')
            client.close()
            break


def enviar_MSG(client, usuario):
    while True:
        try:
            msg = str(input(f'{usuario}(eu): '))
            client.send(f'<{usuario.upper()}> {msg}'.encode('utf-8'))
            if msg == '':
                client.close()
        except:
            return


treinando_socket_cl()







'''def treinando_socket_cl():
    try:
        host = 'localhost'
        door = 50000
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, door))

        info = str(input('Digite a MSG: '))
        s.send(str.encode(info))
        data = s.recv(1024)
        print('Mensagem ecoada:', data.decode())
    except ConnectionRefusedError:
        print('[ERRO] Servidor possivelmente não conectado à rede.')


treinando_socket_cl()'''

