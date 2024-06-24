                                        # CRIANDO MULTIPLAS CONEXÕES ENTRE SERVIDOR E CLIENTES

# python .\server.py ---> para executar o servidor ou outro arquivo pelo terminal com python, depois de inserido o caminho a maneira de se executar é essa.

import threading # para fazer uma função roda do lado da outra.
import socket


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('localhost', 7777))
    except:
        return print('\nNão foi possível se conectar ao servidor\n')

    username = input('Usuário: ')
    print('\Conectado')


# criando Threadigs para que as duas funções rodem ao mesmo tempo (feito por último)
# o parâmetro "target" vai receber o que var ser executado.
    thread1 = threading.Thread(target=recebe_msg, args=[client])
    thread2 = threading.Thread(target=enviar_msg, args=[client, username])

# iniciando as threads (vão rodar ao mesmo tempo)
    thread1.start()
    thread2.start()

def recebe_msg(client):
    while True:  # <- enquanto tiver conectado, o servidor enviará dados.
        try:
            msg = client.recv(2048).decode('utf-8') # a variável 'msg' está recebendo até 2048 bytes.
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor\n') # quando for desconectado do servidor.
            print('Pressione <Enter> para continuar...')
            client.close() # fechar conexão
            break # desconectar-se do servidor


def enviar_msg(client, username):
    while True:
        try:
            msg = input('\n')
            client.send(f'<{username}> {msg}'.encode('utf-8')) # # codificando a mensagem enviada em string para bytes com o método "encode".
        except:
            return


main()

