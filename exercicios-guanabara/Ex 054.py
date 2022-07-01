#EX 054
'''Crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não a maioridade
e quantas já são maiore>.'''

'''from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 7+1):
    nasc = int(input('Digite o ano que nasceu a {} pessoa'.format(c)))
    idade = atual-nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))'''
totalmaior = 0
totalmenor = 0
from datetime import date
atual = date.today().year
for c in range(1, 5):
    nasc = int(input('Digite a data de nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('A total de pessoas maiores de idade é {}'.format(totalmaior))
print('O total de pessoa menores de idade é {}'.format(totalmenor))

























