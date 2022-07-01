#Ex 050
#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#se o valor digitado for ímpar, desconsidere-o

'''s = 0
cont = 0
for c in range(1, 6+1):
    num = int(input('Digite o {} valor: '.format(c)))
    if num %2  == 0:
        s += num
        cont += 1
print('Você informou {} números pares e a soma foi {}'.format(cont, s))'''
s = 0

cont = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        cont = cont+1

print('Você informou {} números pares e a soma é {}'.format(cont, s))





