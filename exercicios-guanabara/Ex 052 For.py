#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''num = int(input('Digite um número: '))
tot = 0
for c in range(1, num+1):

    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO! ')
else:
    print('É por isso ele NÃO é PRIMO!')'''

'''total = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        total += 1
        print('\033[34m', end='')
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\nO número: {} foi divisível {} vezes'.format(num, total))
if total == 2:
    print('Ele é primo!')
else:
    print('Ele não é primo!')'''
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num+1):
    if num % c == 0:
        tot = tot +1
        print('\033[36m', end=' ')
    else:
        print('\033[33m', end=' ')
    print('{}'.format(c), end=' ')
print('\n O número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo!')
else:
    print('Ele náo é primo!')









