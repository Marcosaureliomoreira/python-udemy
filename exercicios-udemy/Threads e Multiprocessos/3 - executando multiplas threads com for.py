import time
import threading

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir():
    print('Indo dormir por 1 segundo...')
    time.sleep(1)
    print('Terminei de dormir...')

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing
threads =[]

# Fazendo um for para cada thread
# quando uso _(underline) no for, significa que não vou usar o contador, ou seja não vou guardar os números dentro de uma variável contadora, mas posso fazer o for atá determinado número.
for _ in range(5):
    thread = threading.Thread(target=dormir)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

final = time.perf_counter() # << Pegar o tempo final

print(f'Rodou em {round(final - inicio, 3)} segundos(s)')

# EXPLICAÇÃO:

# func() <<<<<< 1 segundo >>>>>>> func() <<<<<<<< 1 segundo >>>>>>>> finaliza
# ------------------------------ tempo --------------------------------------

# func() <<<<<<< 1 segundo >>>>>>>>
#        func() <<<<<<<<< 1 segundo >>>>>>>>> finaliza
# -------------- tempo -----------------------------
