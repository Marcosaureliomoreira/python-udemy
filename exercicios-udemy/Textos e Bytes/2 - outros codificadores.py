# Textos e Bytes

# Encoding e decoding

# Duas formas de visualização:
'''
textos --> são os textos que os seres humanos conseguem entender.
bytes--> é a forma que as linguengens de programação, máquinas, conseguem processar e o utf-8 é o codificador
'''

s = 'pelé'
#print(len(s))

# representação em byte:
# utf-8 é o codificador mais usado
# codificando a palavra fácil da variável s:
b = s.encode('utf-8')
print(len(b)) # <<< vai mostrar a quantidade de bytes e caracteres presentes na variável b.

# podemos usar o utf-8, escreve-lo de várias formas:
'''print(s.encode('utf_8'))
print(s.encode('UTF-8'))
'''
# outras formas de codificar uma string:
# codificando:

#print(bytes('pelé', encoding='utf8'))

# ----------------------------------------------------------------------------------------------------------------------

# Outros codificadores

# obs: o UTF-16, codifica tudo, ao contrário do utf-8 que codifica apenas as strings que tem acentos.
# obs: o b que fica na frente, indica que é um byte e não uma string.
# O utf-8 usa forma de codificação em hexadecimal.
# o utf-8 é um pouco mais versátil que o "latim1".


# antigamente o codificador usado era apenas o "ascii" que não suportava acento, então eramos obrigados a digitar sem acentos
print('pele'.encode('ascii'))

print(s.encode('latin1'))

print(s.encode('UTF-8'))
# o UTF-16, codifica tudo, ao contrário do utf-8 que codifica apenas as strings que tem acentos.
print(s.encode('UTF-16'))

