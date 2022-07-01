#Ex 058
#Melhore o desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.Só que o jogador vai tentar advinhar até
#acertar, mostrando no final quantos palpites foram necessários para vencer.

cont = 0
import random
from time import sleep
computador =random.randint(0, 10) #FAZ O COMPUTADOR 'pensar'
print('Vou pensar em um número entre entre 0 e 10. Tente advinhar...')
jogador = int(input('Em que número eu pensei? '))#JOGADOR TENTA ADVINHAR
while jogador != computador:
    cont += 1
    if jogador > computador:
        print('É menos...')
    elif jogador < computador:
        print('É mais...')

    jogador = int(input('Número errado. Tente novamente!'))

print('PARABÉNS! você me venceu, eu pensei no número {} e vc digitou {}'.format(computador, jogador))
print('Foi necessário {} tentativas para vc acertar.'.format(cont))