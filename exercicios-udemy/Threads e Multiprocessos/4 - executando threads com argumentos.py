import time
import threading

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir(segundos):
    print(f'Indo dormir por {segundos} segundo...')
    time.sleep(segundos)
    print(f'Terminei de dormir {segundos} segundos(s)...')

# i/o bound: Momento de espera entre o input(entrada), output(saída). --> threads
# cpu bound: editores de imagens, precessa bastante cpu. --> multiprocessos / multiprocessing
threads =[]

# Fazendo um for para cada thread
for _ in range(5):
    thread = threading.Thread(target=dormir, args=[2])
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

