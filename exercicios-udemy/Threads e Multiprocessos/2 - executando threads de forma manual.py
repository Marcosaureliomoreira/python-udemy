import time
import threading

inicio = time.perf_counter() # << Vai pegar o tempo atual

def dormir():
    print('Indo dormir por 1 segundo...')
    time.sleep(1)
    print('Terminei de dormir...')

# Passando a função para dentro do método threading:
t1 = threading.Thread(target=dormir)
t2 = threading.Thread(target=dormir)

# inciando as threads:
t1.start()
t2.start()

# vai garantir qua as threads abaixo vão terminar antes de executar o restante do código:
t1.join()
t2.join()

final = time.perf_counter() # << Pegar o tempo final

print(f'Rodou em {round(final - inicio, 3)} segundos(s)')

# EXPLICAÇÃO:

# func() <<<<<< 1 segundo >>>>>>> func() <<<<<<<< 1 segundo >>>>>>>> finaliza
# ------------------------------ tempo --------------------------------------

# func() <<<<<<< 1 segundo >>>>>>>>
#        func() <<<<<<<<< 1 segundo >>>>>>>>> finaliza
# -------------- tempo -----------------------------

