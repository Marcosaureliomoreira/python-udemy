
# A imagem tem que estar no mesmo diretório que o código.

with open('hostnet.jpg', 'rb') as hostnet:  # "rb" readbyte - ler bytes
    with open('hostnet_copia.jpg', 'wb') as hostnet_copia:  # "wb" writebytes - escrever bytes
        for byte in hostnet:
            hostnet_copia.write(byte)

