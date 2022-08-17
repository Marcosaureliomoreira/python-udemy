import time
# a biblioteca abaixo tem thread dentro dela
import concurrent.futures

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir(segundos):
    print(f'Indo dormir por {segundos} segundo...')
    time.sleep(segundos)
    return f'Terminei de dormir {segundos} segundos(s)...'

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor: # o ThreadPoolExecutor gera uma piscina de thread.
        segundos = [5,4,3,2,1]
        resultados = [executor.submit(dormir, segundo) for segundo in segundos]

        # as_completed ==> yield resultado devolve o resultado
        for f in concurrent.futures.as_completed(resultados):
            print(f.result()) # << para receber o resultado da função

    final = time.perf_counter() # << Pegar o tempo final
    print(f'Rodou em {round(final-inicio, 3)} segundos(s)')