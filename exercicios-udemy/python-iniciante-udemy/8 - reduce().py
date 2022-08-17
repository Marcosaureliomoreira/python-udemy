# reduce()

# a partir do python 2.7 era nativo
# depois do 3+(do 3 até o momento) não é mais nativo


from functools import reduce

numeros = list(range(1, 11))
print(numeros)

# Função para somar e utiliza-la com reduce:
def soma(x, y):
    return x + y


print(reduce(soma, numeros))


# Função para multiplicar e utiliza-la com reduce:
def multiplica(x, y):
    return x * y


print(reduce(multiplica, numeros))


# multiplicando Utilizando a função lambda:
print(reduce(lambda x, y: x*y, numeros))


# utilizando o for para multiplicar todos os elementos:
produto = 1
for e in numeros:
    produto *= e
print(produto)


