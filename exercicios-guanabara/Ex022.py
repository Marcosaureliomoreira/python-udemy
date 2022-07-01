'''nome = str(input('Digite o seu nome completo:')).strip()
maisculas = nome.upper()
minusculas = nome.lower()
quant = len(nome) - nome.count(' ')
prinome = nome.find(' ')

print('Seu nome em maiscúlas é:{}\nEm minúsculas é:{}\na quantidade de letras é:{} seu primeiro nome é {}'.format(maisculas, minusculas, quant, prinome))'''

nome = str(input('Digite o seu nome completo:')).strip()
print('Seu nome em maiuscúlas é:{}'.format(nome.upper()))
print('Seu nome em minuscúlas é:{}'.format(nome.lower()))
print('Seu nome ao todo tem:{} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem:{} letras'.format(nome.find(' ')))




