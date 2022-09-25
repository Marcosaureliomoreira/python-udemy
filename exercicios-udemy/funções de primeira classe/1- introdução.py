def soma(a,b):
    return a+b



#s = soma(5, 4)

# passando a função soma sem o  esem os parâmetros para a variável s, e depois executando a variável s passando os parâmetros.
# isso é uma função de primeira classe
s = soma
print(s(3, 4))
# -------------------------------------------------------------------------------------------------------------------

# Exemplo 2:

def subtracao(a,b):
    return a-b


sub = subtracao
print(sub(10, 3))
