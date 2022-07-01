# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: INÍCIO, FIM E PASSO. Seu
# programa tem que realizar três contagens através da função criada:
# a)De 1 até 10, de 1 em 1
# b)De 10 até 0, de 2 em 2
# c)Uma contagem personalizada.

'''from time import sleep
def linha():
    print('=' * 30)
def contador(i, f, p):
    if p < 0:
        p *= -1           # linhas especial para não dar problemas no programa.
    if p == 0:
        p = 1
    print(f'A contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end=' ')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')

# Programa principal
contador(0, 10, 1)
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem! ')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''

from time import sleep
def contador(i, f, p):
    if i < f:
        print(f'Contando de {i} até {f} de {p} em {p}')
        sleep(2)
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.4)
            cont += p
        print('FIM')
    else:
        cont = i
        print(f'Contando de {i} até {f} de {p} em {p}')
        sleep(2)
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.4)
            cont -= p
        print('FIM')

ini = int(input('inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo:'))
contador(ini, fim, pas)








contador(0, 10, 1)
contador(10, 0, 2)

