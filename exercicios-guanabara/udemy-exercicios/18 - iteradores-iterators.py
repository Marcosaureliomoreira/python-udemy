"""

- A maioria dos objetos podem ser acessados com o "for":
- O estilo de acessar o loop é claro, consiso e conveniente. O uso de iterators ajudam a unificar o Python. O
que o "for" faz é chamar 0 iter(). A função retorna um objeto iterador que define o método next() que acessa os elemntos um por um
. Quando não existe mais eelemntos, __next__() faz um "raise" da excessão "Stopiteration" que fala para o loop do "for" encerrar.
podemos chamar de método next() usando a função __next__() "built-in";

"""


# Descobrindo como funciona o "for".
# UTILIZANDO O FOR COM ITERATOR:

'''for elemento in [1, 2, 3]:
    print(elemento)

for elemento in (1, 2, 3):
    print(elemento)

for elemento in {'um': 1, 'dois': 2, 'três': 3}:
    print(elemento)

for elemento in '123':
    print(elemento)'''


s = 'abc'
iterador = iter(s)
#print(iterador)

print(next(iterador)) #<< o método "next()" vai pegar o próximo elemento, no caso acima pega o primeiro.
print(next(iterador)) #<< executando novemente vai pegar o segundo elemento. e se "printar" novamente vai pegar o próximo.
print(next(iterador)) # << pegando o terceiro e último elemento. "se printar" novamente var mostrar um erro pos é o último.
print(next(iterador)) # << vai mostrar um  ERRO  de "StopIteration" indicando que é o último elemento.