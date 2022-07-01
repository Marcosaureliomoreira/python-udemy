'''import random
pc= random.randint(0,5)
n = int(input('Em qual número estou pensando?'))

if num == pc:
    print('Parabens vc venceu!')
else:
    print('Você perdeu!')
print(num)'''

import random
from time import sleep
computador =random.randint(0, 5) #FAZ O COMPUTADOR 'pensar'
print('[34Vou pensar em um número entre entre 0 e 5. Tente advinhar...')
jogador = int(input('Em que número eu pensei? '))#JOGADOR TENTA ADVINHAR
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[32mPARABÉNS! Você conseguiu me Vencer!')
else:print('\033[31mGanhei! Eu pensei no número {} e não no número:{}!'.format(computador, jogador))
