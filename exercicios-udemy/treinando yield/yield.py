# ENTENDENDO O yield:
# O yield só pode ser usado dentro de uma função.
# Dentro de uma função ele funciona mais ou menos como um return, com a diferença que ele retorna um generator

# explicação 1:
'''def simpleGeneratorFun():
    for i in range(1, 4):
        yield i


for value in simpleGeneratorFun():
    print(value)'''

# explicação 2:
'''def foo():
   list = [2, 4, 6]

   for x in list:
     yield 2 * x


for value in foo():
    print(value)'''

# explicação 3:
'''def odds(arg):
    for a in arg:
        if a % 2 != 0:
            yield a


items = [100, 101, 102, 103, 104, 105]
for item in odds(items):
    print(item)'''


# explicação 4 (hora de codar):

'''def utilizandoYield(x):
    for i in range(x):
        if (i % 2 == 0):
            yield 'par'
        else:
            yield 'impar'


novogenerator = utilizandoYield(10)
for i in novogenerator:
    print(i)'''

# ----------------------------------------------------------------------------------------------------------------------

# Função que criei para treinar a utilização do "yield"
'''def utilizandoYield(arg):
    for c in arg:
        if c == 27:
            yield 'A sua idade está na lista!'
        


lista_idade = [12, 8, 27, 66, 3]
for i in utilizandoYield(lista_idade):
    print(i)'''



# Outra Função que criei para treinar a utilização do "yield"
'''def utilizandoYield(arg):
    for c in range(arg):
        if c == 27:
            yield 'A sua idade está na lista!'


idade = utilizandoYield(30)
for i in idade:
    print(i)'''


def meuyield():
    lista = [2, 77, 8, 43]
    for numero in lista:
        if numero % 2 == 0:
            yield numero


num = meuyield()
for n in num:
    print(n)
