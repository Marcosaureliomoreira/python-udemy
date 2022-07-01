#Faça um programa que tenha uma função chamada fatorial() que receba dois parâmetros: O primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

'''def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:                      #Significa que é o ultimo número.
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(5, show=True))
help(fatorial)'''





'''def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5,))'''

'''def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))'''



def fatorial(num, show=False):
    f = 1
    for cont in range(num, 0, -1):
        if show:
            print(f'{cont} ', end='')
            if cont > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= cont
    return f

print(fatorial(5))















