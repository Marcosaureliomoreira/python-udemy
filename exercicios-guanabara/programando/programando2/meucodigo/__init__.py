def linha(tam=30):
    print('-' * tam)



def cabecalho(msg):
    linha(40)
    print(msg)
    linha(40)


def numInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except(TypeError, ValueError):
            print('\033[31m[ERRO] digite apenas números!\033[m')
        else:
            return n