# DATETIME

import datetime

# Data e Hora atual (now)

# Mostrando a date e hora atual:
'''print(datetime.datetime.now())'''

# Diferença de Tempo (timedelta)
antes = datetime.datetime.now()

depois = datetime.datetime.now()

diferenca = depois - antes
# vai mostrar a diferença em segundos do tempo de execução do antes e depois.
print(diferenca.seconds)
