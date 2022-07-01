#Crie um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''from time import sleep
from random import randint
lista = list()
jogos = list()
print('-' * 30)
print('      MEGA SENA     ')
print('-' * 30)
quant = int(input('Quantos jogos vc quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *3, f'Sorteando {quant} JOGOS ', '-=' *3)
for i, l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')
    sleep(1)
print('-=' *5, 'BOA SORTE! >', '-=' *5)'''




'''from random import randint
from time import sleep
lista = list()
jogos = list()
cont = 0
quant = int(input('Quantos números quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-' * 3, 'SORTEANDO JOGOS', '-' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i}: {l}')
'''

from random import randint
lista = []
jogos = []
quant = int(input('Quantos jogos que que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('SORTEANDO JOGOS')
for i, v in enumerate(jogos):
    print(f'Jogo {i}: {v}')






























