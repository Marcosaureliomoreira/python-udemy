import collections

lista_de_palavras = 'algumas palavras a serem contadas\ ' \
                     'vou repetir algumas palavras, porque\ ' \
                     'quero ter bastante palavras'.split()

# vai contar quantas vezes aparece cada palavra dentro do texto.
# se removermos o método "split" vai contar quantas vezes aparece cada letra no texto.
counter_freq = collections.Counter(lista_de_palavras)
print(counter_freq)

