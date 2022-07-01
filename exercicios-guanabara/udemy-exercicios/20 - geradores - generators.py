
# Geradores (Generators)
"""
Generators é uma ferramenta simples e poderosa para criar iterators. Eles são escritos como funcões comuns,
porém usam o "Yield" sempre que eles precisam retornar dados. Cada vez que chama o next(), o gerador pausa aonde
parou (e lembra todos e qual o último valor executado).
"""

def inverso(dados):
    for index in range(len(dados)-1, -1, -1): # o "for" possui: start | stop | step
        yield dados[index]


for elemento in inverso('raul'):
    print(elemento)