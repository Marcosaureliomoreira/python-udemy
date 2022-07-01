#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
#a) Quantos números foram digitados.
#b) A lista de valores, ordenada de forma decrescente.
#c) Se o número 5 foi digitado e esta ou não na lista.

'''lista = []
contcinco = 0
while True:
    lista.append(int(input('Digite um número: ')))
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break
print(f'Foram digitados no total {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
if 5 in lista:
    print('O números 5 faz parte da lista')
else:
    print('O número 5 não doi encontrado na lista!')'''


'''lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    tipo = ' '
    while tipo not in 'SN':
        tipo = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if tipo == 'N':
        break

print(f'Foram digitados no total {len(lista)} números')
lista.sort(reverse=True)
print(f'Os Números em ordem decrescente é {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')'''









