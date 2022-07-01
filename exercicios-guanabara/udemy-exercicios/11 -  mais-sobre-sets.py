
# O USO DO SET.
a = ['maçã', 'laranja', 'cenoura', 'laranja', 'pera', 'maçã']
# acima a lista possui frutas repetidas, porém podemos pegar somente as frutas que não são repetidas. veja abaixo:
#print(set(a))

b = ['laranja', 'pera', 'cenoura', 'batata', 'batata']
#print(set(b))

print(set(a) & set(b)) # Para comparar as frutas que tem em comun nas duas listas. (interseção)
print(set(a).intersection(set(b))) # Ou podemos fazer dessa forma e vamos obter o mesmo resultado.

meu_set = {1, 2}
meu_set.remove(1) # Para remover elementos com o método "set".
print(meu_set)
meu_set.add(3) # Adicionando elementos no "set" com "add"
print(meu_set)

# "set" vazio(sem nenhum elemento) é set().


def incomun(a, b):
    """

    :param a: Primeira lista
    :param b: Segunda lista
    :return: Elemento(s) em comun entre as listas
    """
    i = set(a) & set(b)
    return i


d1 = ['a', 'b', 'c', 'd']
d2 = ['a', 'e', 'i', 'u']
print(incomun(d1, d2))















