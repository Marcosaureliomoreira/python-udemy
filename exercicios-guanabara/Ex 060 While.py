#Ex 060
#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex:
#5! = 5x4x3x2x1 = 120     FAZER COM WHILE E COM FOR.

'''from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))'''                   #<<<<<Cálculo usando a bibliotéca matemática para cálcuçlo fatorial


'''n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''
from time import sleep
from math import factorial
num = int(input('Digite um número para calcular o seu fatorial'))
f = factorial(num)
print('Calculando...')
sleep(2)
print('O farial de {} é {}'.format(num, f))
