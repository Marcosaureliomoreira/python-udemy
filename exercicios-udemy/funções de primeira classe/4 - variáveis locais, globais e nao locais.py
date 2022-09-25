# Variáveis locais, globais e não locais V2

def f1(a):
    print(a)
    print(b)


# o b se tornou umá variável global, para poder executar a função acima sem dar erro:
b = 7
f1(9)


b = 5


# --------------------------------------

def f2(a):
    global b
    print(a)
    print(b)
    # se passar o b como no exemplo comentado abeixo vai dar erro, para isso nao acontecer temos que colocar a palavra "global" como acima
    b = 1


f2(3)
# se consultar-mos o b agora vai contar que é 1
print(b)