
# getalmente uma função lambda é executado em uma variável, ou através de um método de aplicar(map) entre outras

ola = lambda : print('Olá')
#ola() # << chamando o método lambda acima


# Fazendo usando uma função ao invés de Lambda:
def eleva_ao_quadrado(x):
    return x**2


#print(eleva_ao_quadrado(4))
#-----------------------------------------------------------------------------------------------------------------------

# quando temos uma função com poucos argumentos, e logo tem um retorno(return) podemos usar a expressão Lambda.

# usando Lambda para fazer a mesma coisa que a função acima:

'''aoquadrado = lambda x: x**2  # << expressões lambda são digitadas em apenas uma linha, éssa é uma das regras.
print(aoquadrado(3))
'''

#SOMANDO NÚMEROS:

# FAZENDO SEM A LAMBDA:
'''def soma_dois_numeros(a,b):
    return a+b


print(soma_dois_numeros(2, 3))'''


# FAZENDO COM O LAMBDA:
'''soma = lambda a, b: a + b
print(soma(2, 3))'''
#=======================================================================================================================

# VERIFICADO NÚMERO PAR OU ÍMPAR

# Fazendo com função: (Sem Lambda)
'''def impar_ou_par(num):
    if num %2 == 0:
        print(f'{num} é par')
    else:
        print(f'{num} é impar')


impar_ou_par(1)
'''

# Fazendo com expressão Lambda:
# abaixo estamos utilizando if e else na mesma linha:
par_impar = lambda num: print(f'{num} é par') if num %2 == 0 else print(f'{num} é ímpar')
par_impar(2019)

