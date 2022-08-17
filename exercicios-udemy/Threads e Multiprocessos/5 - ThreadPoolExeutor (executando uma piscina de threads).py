# UTILIZANDO A FORMA MAIS PRATICA DE SE FAZER:

import time
# a biblioteca abaixo tem thread dentro dela
import concurrent.futures

'''inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir(segundos):
    print(f'Indo dormir por {segundos} segundo...')
    time.sleep(segundos)
    return f'Terminei de dormir {segundos} segundos(s)...'

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(dormir, 1) # enviando a função e quantidade de tempo que queremos que durma
        f2 = executor.submit(dormir, 1)

        print(f1.result()) # << para receber o resultado da função
        print(f1.result())

    final = time.perf_counter() # << Pegar o tempo final

    print(f'Rodou em {round(final - inicio, 3)} segundos(s)')
'''



# utilizando o for:

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir(segundos):
    print(f'Indo dormir por {segundos} segundo...')
    time.sleep(segundos)
    return f'Terminei de dormir {segundos} segundos(s)...'

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor: # o ThreadPoolExecutor gera uma piscina de thread.
        resultados = [executor.submit(dormir, 1) for _ in range(5)]

        # as_completed ==> yield resultado devolve o resultado
        for f in concurrent.futures.as_completed(resultados):
            print(f.result()) # << para receber o resultado da função

    final = time.perf_counter() # << Pegar o tempo final
    print(f'Rodou em {round(final-inicio, 3)} segundos(s)')