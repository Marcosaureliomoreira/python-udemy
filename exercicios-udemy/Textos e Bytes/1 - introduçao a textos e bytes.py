# Textos e Bytes

# Encoding e decoding

# Duas formas de visualização:
'''
textos --> são os textos que os seres humanos conseguem entender.
bytes--> é a forma que as linguengens de programação, máquinas, conseguem processar e o utf-8 é o codificador
'''

s = 'fácil'
print(len(s))

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

print(bytes('pelé', encoding='utf8'))


