import time
import threading

inicio = time.perf_counter()

def interacao(num):
    cont = 0
    lista = []
    print('Começando...')
    for _ in range(3):
        n1 = int(input(num))
        cont += 1
        lista.append(n1)


    print(f'Foram digitados {cont} números')
    print(f'Os números digitados foram: ', end='')
    for n in lista:
        print(n, end=' ')


nu = interacao("Número: ")

final = time.perf_counter()
print(f'\nA aplicação Rodou em {round(final-inicio, 3)} segundos(s)')
