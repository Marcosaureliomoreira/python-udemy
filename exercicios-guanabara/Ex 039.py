#Ex 039
'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
-Se ele ainda vai se alistar ao serviço militar.
-Se é hora de ele se alistar.
-Se ja passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

'''nascimento = int(input('Digite o ano do nascimento: '))

if nascimento >2003:
    print('Você ainda vai se alistar!')
elif nascimento == 2003:
    print('É hora de se alistar!')
else:
    print('Já passou da hora de se alistar!')'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(saldo))

elif idade > 18:
    saldo = idade -18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))






