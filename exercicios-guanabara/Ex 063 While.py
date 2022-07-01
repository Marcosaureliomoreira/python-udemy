#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
#Exemplo: 0 1 1 2 3 5 8.

'''print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos quer digitar? '))
t1 = 0
t2 = 1
print('~' * 30)
print('{} {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(', {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont+= 1
print(', FIM')
print('~' * 30)'''
print('-=' * 12)
print('Sequencia de Fibonacci')
n = int(input('Quantos termos quer digitar? '))

e1 = 0
e2 = 1
cont = 3
print('{} {}'.format(e1, e2), end='')
while cont <= n:
    e3 = e1 + e2
    print(' {}'.format(e3), end='')
    e1 = e2
    e2 = e3
    cont += 1
print(', Fim')










