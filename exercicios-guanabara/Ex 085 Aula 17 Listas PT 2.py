#Crie um programa onde o usuário possa sete valores numéricos e cadastre-os e uma lista única que mantenha separado os
# valores pares e ímpares. No final mostre os valores pares em ordem crescente.

'''lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor %2 == 0:
        lista[0].append(valor)
    elif valor %2 == 1:
        lista[1].append(valor)
lista[0].sort()
print(f'O valores pares são: {lista[0]}')
print(f'Os valores ínpares são: {lista[1]}')'''

777


pilha = [[], []]
cont = 0
for c in range(0, 7):
    num = int(input('Digite o valor: '))
    if num %2 == 0:
        pilha[0].append(num)
    elif num %2 == 1:
        pilha[1].append(num)
    cont += 1
pilha[0].sort()
print(f'A quantidade de valores é {cont}')
print(f'Os valores pares digitados foram {pilha[0]}')
print(f'Os valores ímpares digitados foram {pilha[1]}')
print(f'O maior valor digitado na lista de pares foi {max(pilha[0])}')


















