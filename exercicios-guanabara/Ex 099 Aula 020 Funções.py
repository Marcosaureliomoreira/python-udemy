# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com o valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def linha():
    print('-' *30)
def maior(* num):
    cont = maior = 0
    linha()
    print(f'Analizando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}.')


maior(1, 3, 6, 17)
maior(34, 26, 2, 45, 22)
maior(44, 90, 43)


