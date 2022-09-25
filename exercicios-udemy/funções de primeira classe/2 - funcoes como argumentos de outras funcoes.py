def soma(a,b):
    return a+b



#s = soma(5, 4)

# passando a função soma sem o  esem os parâmetros para a variável s, e depois executando a variável s passando os parâmetros.
# isso é uma função de primeira classe
s = soma
#print(s(3, 4))
# -------------------------------------------------------------------------------------------------------------------

# Exemplo 2:

def subtracao(a,b):
    return a-b


sub = subtracao
print(sub(10, 3))


# -----------------------------------------------------------------------------------------------------------------------

# funções como argumento de outras funções:

def minha_func(func, lista):
    resultado = []
    for a,b in lista:
        resultado.append(func(a,b))
    return resultado


# usando a função subtração criada anteriormente para dentro da função minha_func:
subs = minha_func(subtracao, [(3,2), (4,6), (6,4), (10,8)])
print(subs)



# Exemplo 2:
# # usando a função soma criada anteriormente para dentro da função minha_func:
subs = minha_func(soma, [(3,2), (4,6), (6,4), (10,8)])
print(subs)
