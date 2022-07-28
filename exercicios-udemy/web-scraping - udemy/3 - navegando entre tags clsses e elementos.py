import requests
from bs4 import BeautifulSoup

resposta = requests.get('http://127.0.0.1:5000/')
#verificando o status code, se é 200, se há conexão.
print(resposta)

# Obtendo acesso ao html do site.
#print(resposta.text)

"""
acessando cada elemento individualmente:
através do "Beautufulsoup podemos acessar cada tag dentro do html"
'html.parser' estrutura da pagina html, poderia ser também 'lxml'.
"""
soup = BeautifulSoup(resposta.text, 'html.parser')

# "prettify" significa embelezar, vai mostrar a estrutura da página html com a identação.
#print(soup.prettify())

# buscando o titulo da página através da tag, "find" é encontrar.
#print(soup.find('title'))

# Vai mostrar somente o texto sem a tag.
#print(soup.find('title').text)

# buscando através de uma classe, no caso abaixo, a classe post:
#print(soup.find(class_='post'))

# buscando todas as classes na página com método "find_all", vai retornar uma lista,
# assim podemos acessar por indices, exemplo: print(soup.find_all(class_='post')[0]) e acessar cada classe como se fosse uma lista.
#print(soup.find_all(class_='post'))

# Acessando somente o titulo do segundo elemento da lista que foi retornada da classe "post":
#print(soup.find_all(class_='post')[1].find('h3'))

# Acessando um link da segunda classe "post" dentro do "href":
print(soup.find_all(class_='post')[1].find('a')['href'])



