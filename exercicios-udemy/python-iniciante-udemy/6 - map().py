
# map, filter e reduce

# map:

numeros = list(range(1, 11))
print(numeros)

# usando o map para elevar cada elemento da lista ao quadrado:

def quadrado(x):
    return x ** 2

# map com função:
print(list(map(quadrado, numeros))) # <<< vai retornar a lista de números anteriores ao quadrado

#-----------------------------------------------------------------------------------------------------------------------


# retornando uma lista de números ao quadrado com map com lambda:
print(list(map(lambda x: x**2, numeros)))

#-----------------------------------------------------------------------------------------------------------------------

# Fazendo com compreensão de lista:

print([x**2 for x in numeros])


# for normal:
nova_lista = []
for n in numeros:
    nova_lista.append(n**2)
print(nova_lista)
