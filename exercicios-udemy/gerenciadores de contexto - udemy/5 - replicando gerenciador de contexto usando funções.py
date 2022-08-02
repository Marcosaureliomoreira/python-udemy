# Gerencciador de contexto usando Funções:

#.Com Funções:
# Usando funções combinadas com depurador:
# É como se estivessemos criando o nosso próprio gerencador de contexto ou mostrando como funciona um.

from contextlib import contextmanager

'''#depurador:
@contextmanager
def abrir(arquivo, modo):
    f = open(arquivo, modo) # __enter__
    yield f # vai retornar o f com o with
    f.close() # __exit__

with abrir('arquivos/exemplo3.txt', 'w') as f:
    f.write('exemplo 3')'''


# Com try e finally:
#depurador:
@contextmanager
def abrir(arquivo, modo):
    try:
        f = open(arquivo, modo) # __enter__
        yield f # vai retornar o f com o with
    # com o "finally" é garantido que o arquivo feche, mesmo se der erro.
    finally:
        f.close() # __exit__


with abrir('arquivos/exemplo3.txt', 'w') as f:
    f.write('exemplo 3')

