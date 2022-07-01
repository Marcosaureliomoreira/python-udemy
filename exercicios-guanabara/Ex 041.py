#Ex 041
'''a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-Até 9 anos: MIRIM
-Até 14 anos: INFANTIL
-Até 19 anos: SÊNIOR
-Acima: MASTER'''

from datetime import date
atual = date .today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('\033[36mAtleta MIRIM')
elif idade <= 14:
    print('\033[32mAtleta INFANTIL')
elif idade <= 19:
    print('\033[33mAtleta JUNIOR')
elif idade <= 25:
    print('\033[35mAtleta SÊNIOR')
else:
    print('\033[31mAtleta MASTER')








