#memoryview() - Leitura de imagens

# lendo imagem:
with open('hostnet.jpg', 'rb') as f:
    hostnet = memoryview(f.read())

# vefificando o tamanho da imagem em byte:
print(len(hostnet))

# fazendo um slicing de 10 bytes
# assim que o computador interpreta uma imagem... em bytes.
img = bytes(hostnet[:10])
#print(img)

# tentando decodificar, porém vai dar erro, por isso usamos o "replace" para mostrar onde está o erro:
print(img.decode('utf8', 'replace'))


