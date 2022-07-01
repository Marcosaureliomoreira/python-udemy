#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#a)Quantas pessoas foram cadastradas.
#b)Uma listagem com as pessoas mais pesadas.
#c)Uma listagem com as pessoas mais leves.

'''pessoas = list()
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S para sim, N para não] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os dados foram {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso cadastrado foi {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'O menor peso cadastrado foi {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()'''


'''pessoas = list()
dados = list()
cont = maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S para sim, N para não] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Os dados foram {pessoas}')
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}Kg de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'O menor peso digitado foi {menor}Kg de' , end='' )
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')'''





'''maiorpeso = list()
fixa = list()
temp = list()
cont = maior = cont = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(fixa) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    fixa.append(temp[:])
    temp.clear()
    cont += 1
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {maior}Kg de ', end='')
for p in fixa:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'O menor peso foi {menor}Kg de ', end='')
for p in fixa:
    if p[1] == menor:
        print(f'{p[0]} ', end='')'''


'''lista = []
tempo = []
quantp = maior = menor = 0
while True:
    tempo.append(str(input('Nome: ')))
    tempo.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = tempo[1]
    else:
        if tempo[1] > maior:
            maior = tempo[1]
        if tempo[1] < menor:
            menor = tempo[1]

    lista.append(tempo[:])
    tempo.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'A quantidade de pessoas cadastradas foi {len(lista)}')
print(f'O maior peso digitado foi {maior}Kg. de ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print(f'\nO menor peso digitado foi {menor}. de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}', end='')'''











lista = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input("Peso: ")))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [SN]')).upper().strip()[0]
    if tipo == 'N':
        break
print(f'A quantidade de pessoas cadstradas na minha lista é {len(lista)}')
print(f'O maior peso da lista foi {maior}Kg. de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print(f'O menor peso da lista é {menor}Kg. de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]} ', end='')








