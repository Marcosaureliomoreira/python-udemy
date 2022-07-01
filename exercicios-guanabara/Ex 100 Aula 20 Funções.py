#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somapar(). A primeira função
# vai sortear 5 números e vai colocalas dentro da lista e a sugunda função vai mostrar a soma de todos os valores pares
# sorteados pela função anterior.
from random import  randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.4)

def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'\nSomando todos os valores pares de {lista} temos {soma}')

números = list()
sorteia(números)
somapar(números)

