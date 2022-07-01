'''n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2) /2

print('A média entre:{} e {} é igual a {}'.format(n1, n2, media))'''


'''nome = str(input('Digite o nome:')).upper()
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))

media = (n1 + n2 )/2
print('Olá {} a média entre suas respectivas notas:{} e {} é igual a {}'.format(nome, n1, n2, media))'''
media= 0
soma = 0
nome = str(input('Digite o nome:')).upper()
for c in range(1,3):
    notas = float(input('Digite as notas:'))
    soma = notas + soma
    media = (notas + soma) /2

print('A soma das duas notas é {}'.format(soma))
print('A médias das notas é {}'.format(media))









