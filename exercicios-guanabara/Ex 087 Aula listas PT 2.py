#Aprimore o desafio anterior, mostrando no final:
#a)A soma de todos os valores digitados.
#b)A soma dos valores da tereira coluna.
#c)O maior valor da segunda coluna.

'''soma = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = maior = scol = 0
for linha in range(0,3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] %2 == 0:
            spar += matriz[linha][coluna]
    print()
print(f'A soma dos valores pares é {spar}')
for linha in range(0, 3):
    scol += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')'''



somapar = somacol = maior = menor = 0
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para cada posição [{linha}, {coluna}] '))
        if matriz[linha][coluna] %2 == 0:
            somapar += matriz[linha][coluna]
for linha in range(0, 3):
    somacol += matriz[linha][2]
    for coluna in range(0, 3):
        if coluna == 0:
            maior = manor = matriz[1][coluna]
        else:
            if matriz[1][coluna] > maior:
                maior = matriz[1][coluna]
            if matriz[1][coluna] < menor:
                menor = matriz[1][coluna]


        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A Soma dos valores pares digitados é: {somapar}')
print(f'a soma dos valores da terceira coluna é {somacol}')
print(f'O maior valor da terceira coluna é {maior}')
