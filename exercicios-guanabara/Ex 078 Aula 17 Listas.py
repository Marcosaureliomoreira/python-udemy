
#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor
#digitado e as suas respectivas posições na lista.
'''maior = 0
menor = 0
lista = []
for cont in range(0, 5):
    lista.append(int(input(f'Digite um número na posição: {cont} ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print(f'VocÊ digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...' , end='')
print(f'O menor valor digitado foi {menor} nas posições ' , end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}, ', end='')'''





'''tabela = []
maior = 0
menor = 0
for c in range(0, 5):
    tabela.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = tabela[c]
    else:
        if tabela[c] > maior:
            maior = tabela[c]
        if tabela[c] < menor:
            menor = tabela[c]
print(f'Você digitou os números: {tabela}')
print(f'O maior número digitado foi {maior} nas posições ', end='')
for pos, v in enumerate(tabela):
    if v == maior:
        print(f'{pos} ' , end='')
print(f'\nO menor número digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(tabela):
    if v == menor:
        print(f'{pos} ' , end='')'''


'''lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite um número na posição {c} ')))
    if c == 1:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'Você digitou os números {lista}')
print(f'O maior digitado foi {maior} na posição ', end='')
for pos , v in enumerate(lista):
    if v == maior:
        print(f'{pos}', end=' ')
print(f'\nO menor número digitado foi {menor} nas posições ', end='')
for pos, v in enumerate(lista):
    if v == menor:
        print(f'{pos} ', end='')'''


numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um número: {c} ')))
    if c == 1:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f'Os valores digitados foram {numeros}')
print(f'O maior número digitado foi {maior} na posição ', end='')
for pos, v in enumerate(numeros):
    if v == maior:
        print(f'{pos} ', end='')
print(f'O menor valor digitado foi {menor} na posição ', end='')
for pos, v in enumerate(numeros):
    if v == menor:
        print(f'{pos} ', end='')






