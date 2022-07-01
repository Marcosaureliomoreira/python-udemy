
"""
- O escopo interno, o qual é pesquisado primeiro contém nomes locais
- O escopo de uma função, considerando que o nome ja existe de forma local,contém nomes não-locais (nonlocal)
e mas também não globais.
- O escopo externo contém variáveis globas (global)
- O último escopo, pesquisado por último são os nomes buit-ins, do próprio python.
"""

# Definindo uma variável não-local:

'''def teste_escopo():
    #variavel = 'local'  # sem a variável local teriamos um ERRO.
    def atr_nonlocal():
        nonlocal variavel
        variavel = 'nonlocal'''


def teste_escopo():
    def atr_local():
        variavel = 'local'    # << Variável local

    def atr_nonlocal():
        nonlocal variavel     # << Variável não-local
        variavel = 'nonlocal'

    def atr_global():
        global variavel
        variavel = 'global'   # << Variável global


    atr_local()
    variavel ='outro'
    print('local', variavel)

    atr_nonlocal()
    print('nonlocal', variavel)

    atr_global()
    print('global', variavel)

teste_escopo()
