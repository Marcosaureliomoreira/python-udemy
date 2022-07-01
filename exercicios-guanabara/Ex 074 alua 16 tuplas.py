#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagens de números gerados e também indique o menor e o maior valor qua estão na tupla.

#from random import randint
'''cont = maior = menor = 0
numeros = (randint(1, 6), randint(1, 6,), randint(1, 6,),
     randint(1, 6,), randint(1, 6, ))
#print(f'Os números sorteados foram {numeros}')
#print(f'O maior valor sorteado foi {max(numeros)}')
#print(f'O menor valor sorteado foi {min(numeros)}')

print('Os númros sorteados foram: ', end='')
for n in numeros:            #<<<Para cada número em números.
     print(f'{n} ', end='')
print(f'\nO maior valor digitado foi:{max(numeros)}')
print(f'O menor valor digitado foi {min(numeros)}')'''




'''from random import randint
numeros = (randint(1, 6), randint(1, 6,), randint(1, 6,),
     randint(1, 6,), randint(1, 6, ))

print('Os números gerados foram ', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior números foi:{max(numeros)}')
print(f'O menor número foi:{min(numeros)}'''''


from random import randint
numeros = (randint(1, 6), randint(1, 6,), randint(1, 6,),
     randint(1, 6,), randint(1, 6, ))
print(f'Os números gerados foram ' , end=' ' )
for n in numeros:
    print(f'{n}, ' , end='')
















