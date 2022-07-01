#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) quantas vezes apareceu o valor 9.
# b) em que posição foi digitado o primeiro valor 3.
# c) Quai foram os números pares.
'''num = cont = contpar = 0
valores = ('0', '1', '2', '3', '4')
for c in range(1, 5):
    num = int(input('Digite um número: '))
    if num == 9:
        cont +=1
    elif num == 0:
        num = 0
    if num %2 == 0:
        contpar += 1
print(f'Você digitou os valores {num}')
print(f'O Número 9 apareceu {cont} vezes')
print(f'Números pares digitados foram {contpar}')'''


'''num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
       print(f'O número 3 aparece na posição {num.index(3)+1}')
else:
       print('O valor 3 não aparece em nenhuma posição')
print(f'Os números pares digitados foram ', end=' ')
for n in num:
       if n %2 == 0:
              print(n, end=' ')'''




num = (int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')),
       int(input('Digite um número: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
       print(f'O valor 3 foi digitado na posição {num.index(3)+1}')
else:
       print('O número 3 não se encontra em nenhuma posição.')
print('Os números pares Digitados foram ', end='')
for n in num:
       if n %2 == 0:
              print(n, end='')
