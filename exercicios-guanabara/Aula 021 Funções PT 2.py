#Interactive help. AJUDA INTERATIVA DO PYTHON, COMO NO EXEPLO ABAIXO.

'''help(print)
help(input)
#Podemos fazer também de uma forma diferente.
print(input.__doc__)'''

#=======================================================================================================================

# DOCSTRINGS
'''def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da passagem
    :param p: passo da contagem
    :return: sem retorno
    Função criado por Marcos Aurélio.
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c += p
    print('FIM!')
help(contador)
contador(2, 10, 2)'''

#=======================================================================================================================

#PARÂMETROS OPCIONAIS:
'''def somar(a, b, c=0):
    """
    > Faz a soma de três valores e mostra o resultado na tela.
    :param a: O primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return:
    """
    s = a + b + c
    print(f'A soma dos valores é {s}')

somar(7, 1)'''
# *O A vai receber 7 e o B vai receber 1, e o C vai receber 0, Já que está recebendo valor opcional.
# *Podemos colocar também todos os parâmetros como opcional.

#=======================================================================================================================

# ESCOPO DE VARIÁVEIS
'''def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')


#programa principal
n = 2
print(f'No programa principal, n valor {n}')
teste()
#print(f'No programa principal, x vale {x}')'''

'''def função():
    n1 = 10
    print(f'n1 dentro vale {n1}')

n1 = 2
função()
print(f'n1 fora vale {n1}')'''

'''def teste(b):
    global a
    a = 8
    b += 4 
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {c}')
    print(f'C dentro vale {c}')
    
#A variável 'A' que valia 5, agora vale 8. porque foi chamada a função global dentro da função teste. Então ela utiliza a 
# variável local como referência. com isso a variável "a" que valia 5 foi apagada e agora vale 8.

a = 5
teste(a)
print(f'S fora vale {a}')'''
#=======================================================================================================================

# RETORNANDO VALORES

'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s



r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')'''
#=======================================================================================================================

#                                               PARTE PRÁTICA
#Usando a Função 'return'

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

#n = int(input('Digite um número: '))
#print(f'O fatorial de {n} é igual a {fatorial(n)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são: {f1}, {f2}, {f3}')



'''def par (n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')'''




