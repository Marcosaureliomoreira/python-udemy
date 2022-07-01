#Aula 012 - condições aninhadas.
nome = str(input('Qual é seu nome?'))
if nome == 'Marcos':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é muito popular aqui no Brasil.')
elif nome in 'André Gustavo Renato Hugo':
    print('Belo nome Masculino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))


