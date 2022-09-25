# Lidando com erros de Encoding

mae = 'mãe'
#print(mae.encode('ascii'))

# Também é limitado a caracteres comuns:
#print(mae.encode('cp437'))

# vai ignorar os caracteres que possuam acentuações, por conta do método "ignore", com isso perde dados
# não é a forma adequada a se fazer.
#print(mae.encode('cp437', 'ignore'))

# com o método "replace" vai sibstituir a objeto caractere que não conseguiu codificar por um ponto de interrogação como no exemplo abaixo:
# com essa opção, perdemos dados porém sabemos que temos erro
#print(mae.encode('cp437', 'replace'))

# o método abaixo substitui por contrabarra onde não foi codificado:
#print(mae.encode('cp437', 'backslashreplace'))


# o método abaixo explica qual a string que ele não conseguiu processar, ou seja substitui por explicação do caracter
#print(mae.encode('cp437', 'namereplace'))

# o método abaixo substitui por um xml de referência
#print(mae.encode('cp437', 'xmlcharrefreplace'))


# Decodificando uma string xml:

import lxml.html

# vai decodificar a string mae
mae_xml = lxml.html.fromstring(mae).text
print(mae)





