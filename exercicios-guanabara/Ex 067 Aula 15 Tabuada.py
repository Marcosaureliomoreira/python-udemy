#Crie um programa que leia a tabuada de vários números inteiros, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

'''num = int(input('Digite um mnúmero: '))     #Tabuada feita da maneira convencional
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('-' * 12)

num = int(input('Digite um número para ver a sua tabuada: '))     #Tabuada feita com for.
for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num*c))'''

while True:
    num = int(input('Quer ver a tabuada de qual valor? : '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')

print('Fim')



























