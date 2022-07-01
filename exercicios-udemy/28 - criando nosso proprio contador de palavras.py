
lista_de_palavras = """bastante algumas porque palavras a serem quero contadas
vou repetir palavras algumas palavras, porque
quero ter bastante palavras""".split()

novo_texto = """
bastante algumas porque palavras a serem quero contadas
vou repetir palavras algumas palavras, porque
quero ter bastante palavras
"""

with open('novo_texto.txt', 'w') as nt:
    nt.write(novo_texto)

'''with open('novo_texto.txt') as texto:
    for linha in texto:
        print(linha, end='')'''


import re


index = {}
p = re.compile(r'\w+')
with open('novo_texto.txt') as texto:
    for n_linha, linha in enumerate(texto, 1): # pegando a linha e a posição de cada em texto, começando no 1.
        for match in p.finditer(linha):
            palavra = match.group()
            localizacao = (n_linha, match.span()) # "span()" é o índice do começo e o índice do final.

            # 1 Versão
            #ocorrencias = index.get(palavra, [])
            #ocorrencias.append(localizacao)
            #index[palavra] = ocorrencias

            # 2 Versão
            #if palavra not in index:  # se não existe palavra vai criar uma lista.
            #    index[palavra] = []
            #index[palavra].append(localizacao) # senão, se existe palavra, vai adiciona-la e sua localização.

            # 3 Versão
            index.setdefault(palavra, []).append(localizacao)

        palavra_freq = []
        for palavra in sorted(index, key=str.upper):
            print(palavra, len(index[palavra]))
            palavra_freq.append((palavra, len(index[palavra])))

print(palavra_freq) #retornando uma tupla com o mesmo resultado.

print(dict(palavra_freq)) # convertendo para dicionário.

#_______________________________________________________________________________________________________________________

#pip install wordcloud (FALTA INSTALAR)
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nuvem = WordCloud(background_color='white')

plt.figure(figsize=(12,8), dpi=300)
nuvem.generate_from_frequencies(dict(palavra_freq))
plt.imshow(nuvem)
plt.axis('off')
plt.show()
