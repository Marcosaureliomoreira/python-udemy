#Ex 038
'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são iguais.'''
from time import sleep
p1 = int(input('Digite o primeiro número: '))
p2 = int(input('Digite o segundo núemero: '))
sleep(2)
if p1 > p2:
    print('O PRIMEIRO número é maior!')
elif p2 > p1:
    print('O SEGUNDO número digitado é maior!')
else:
    print('Não existe valor maior, numeros Digitados são IGUAIS!')




