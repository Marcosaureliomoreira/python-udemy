# __anotations__dir()

# esses dois pontos + o tipo primitivo(: int) ao lado dos parâmetros dentro da função abaixo, é uma explicação(anotação) sobre o tipo do parâmetro.
def soma(a: int, b: int):
    """soma a + b"""
    return a + b


# Acessando o docstring:
print(soma.__doc__)

# Vai mostrar tudo o que podemos chamar desta função:
#print(dir(soma))

# Mostra anotações sobre a função, caso não tenha anotação vai retornar um disionário vázio:
#print(soma.__annotations__)

# Mostra o nome da função:
#print(soma.__name__)

# ----------------------------------------------------------------------------------------------------------------------


# Criando uma função Qualquer:
def f(a: str = '', b: int = 0, c: float = None, d: bool = None):
    """minha função mista"""

    print(f.__annotations__)


print(f('a', 1, 4.3, False))
print(f())


import math

# Importando biblioteca e buscando informações sobre ela:
print(dir(math))

# Mostra a raiz quadrada de 9:
print(math.sqrt(9))

# Mostra o sêno de 30:
print(math.sin(30))

# mostra a documentação do match.pow:
#print(math.pow.__doc__)

# mostra 4 elevado a 3:
print(math.pow(4, 3))
