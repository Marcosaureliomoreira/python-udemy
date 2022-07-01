#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e ímpares digitados, respectivamente. ao final, mostre o conteúdo das três listas geradas.

lista = []
listapar = []
listaimpar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    resp =' '
    if num %2 == 0:
        listapar.append(num)
    if num %2 == 1:
        listaimpar.append(num)
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print('=' *40)
print(f'Os números digitados foram {lista}')
print(f'A lista dos números pares digitados foram {listapar}')
print(f'A lista dos números ímpares digitados foram {listaimpar}')




'''lista = []
listapar = []
listaimpar = []
mai = men = cont = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)

    if num %2 == 0:
        listapar.append(num)
    elif num %2 == 1:
        listaimpar.append(num)
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break


print(f'Os números digitados foram: {lista}')
print(f'A lista dos números pares é {listapar}')
print(f'A lista dos números ímpares é {listaimpar}')
print(f'O maior números foi {max(lista)}')
print(f'A quantidade de elementos digitados foi {len(lista)}')'''
