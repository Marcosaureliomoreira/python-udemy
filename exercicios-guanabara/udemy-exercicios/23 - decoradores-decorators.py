"""
- O functools significa uma função dentro da outra.
"""

import functools

def meu_decorador(func):
    @functools.wraps(func) # wraps significa "embrulhar" a func
    def funcao_que_roda_func():
        print('***************Embrulhando função**************')
        func()
        print('Nome da função:', func.__name__)
        print('************Fechando embrulho************')
    return funcao_que_roda_func


@meu_decorador
def minha_funcao():
    print('Sou uma função')

minha_funcao()

#---------------------------------------------

def decorador(f):
    @functools.wraps(f)
    def decor(c=1, d=1):
        c + d
        print('Olá, Mundo!')
        f(c, d)
    return decor


@decorador
def soma(a=1, b=1):
    s = a + b
    print(f'A soma entre {a} e {b} = {s}')

n1 = 4
n2 = 10
soma(n1, n2)
#------------------------------------------------

def meudecorando(ff):
    @functools.wraps(ff)
    def meu_decor(msg):
        print('Bom Dia!')
        ff(msg)
    return meu_decor


@meudecorando
def maiuscula(frase=''):
    f = frase.upper()
    print(f)


maiuscula('Oi')



