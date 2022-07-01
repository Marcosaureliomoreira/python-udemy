#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar no final. No final, mostre:
# a) Qual o total de gasto na compra.
# b) Quantos produtos custam mais de R$ 1000.
# c) Qual é o nome do produto mais barato.
'''total = produtomil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    preço = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        produtomil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
           menor = preço
           barato = produto
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opção == 'N':
        break
print(f'O total de itens comprados foi R$ {total:.2f} ')
print(f'Temos {produtomil} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')'''

cont = total = totmil = menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuas? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'O total de gastos  é {total:.2f}')
print(f'Temos {totmil} produtos que custam mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')

















