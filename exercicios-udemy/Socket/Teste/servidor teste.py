# criando servidor (teste)

import socket


def main():
    host = 'localhost'
    port = 50000

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((host, port))
        s.listen()
        print('Aguardando conexão...')
        conn, ender = s.accept()
        print('Conectado em: ', ender)
        while True:
            data = conn.recv(1024)
            if not data:
                print('Fechando conexão...')
                conn.close()
                break
            conn.sendall(data)
    except:
        print('\nNão for possível conectar-se ao servidor.\n')



