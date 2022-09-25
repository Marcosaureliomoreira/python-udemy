# Fatiando(Slicing) e indexando Bytes

# bytearray é um inteiro geralmente de 0 a 255

s = 'pelé'
b = s.encode('utf8')
print(b)

# resultado do número inteiro abaixo corresponde ao primeiro elemento, pegando por index:
print(b[0])

# aqui temos uma sequência de bytes
print(b[:1])


