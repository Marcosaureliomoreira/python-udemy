


# Somando dois números:
'''def soma_dois_numeros(arg1, arg2):
    return arg1 + arg2


print(soma_dois_numeros(4, 5))'''


# Passando uma lista de números a serem somados:
'''def lista_somada(lista_itens):
    return sum(lista_itens)


print(lista_somada([10, 5, 3]))'''

#-----------------------------------------------------------------------------------------------------------------------

#                                                     Args e Kwargs


# Somando argumentos uma lista de argumentos sem tamanho fixo(não sabemos quantos são):

'''def soma(*args):
    return sum(args)


print(soma(2, 3, 55, 8, 11, 11, 500))
'''

# Desempacotando args de listas:
# desempacotando a lista na mesma linha:
#print(list(range(1, 10, 2))) # << Passando uma lista e que vai de 1 até 10 pulando de 2 em 2


# desempacotando a lista argumentos:
argumentos = [1, 10, 2]
print(list(range(*argumentos)))


# desempacotando os argumentos da lista arg_tuplas:
arg_tuplas = [1, 20, 2]
print(list(range(*arg_tuplas)))
