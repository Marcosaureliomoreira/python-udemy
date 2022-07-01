#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. caso o números exista lá dentro,
#ele não será adicionado. no final serão exibidos todos os valores únicos digitados, em ordem crescente.
'''numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valoer duplicado, não vou adicionar!')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')'''



numero = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numero:
        numero.append(num)
        print('Número Adicionado...')
    else:
        print('Número duplicado!')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Você digitou os valores {numero}')
