import time

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir():
    print('Indo dormir por 1 segundo...')
    time.sleep(1)
    print('Terminei de dormir...')

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing

dormir() # Chamando a função...
dormir()
dormir()
dormir()

final = time.perf_counter() # << Pegar o tempo final

print(f'Rodou em {round(final - inicio, 3)} segundos(s)') # Calculando em quanto tempo rodou a aplicação. o "round" arredonda o numero de casas decimais, no caso 3.
