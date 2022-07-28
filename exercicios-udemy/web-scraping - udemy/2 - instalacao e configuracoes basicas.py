"""
Beautiful Soup é um pacote Python para analisar documentos HTML e XML.
Ele cria uma árvore de análise para páginas analisadas que podem ser usadas para extrair dados de HTML, o que é útil para web scraping.

"""


 # INSTALAÇÕES NECESSÁRIAS:

 # pip install bs4

 # parsers
 # pip install lxml       (opcional)
 # pip install html5lib   (opcional)
 # pip install requests


# Fazendo webscraping no meu site(site.html)

import requests
from bs4 import BeautifulSoup

resposta = requests.get('http://127.0.0.1:5000/')
#verificando o status code, se é 200.
print(resposta)

# Obtendo acesso ao html do site.
#print(resposta.text)

# acessando cada elemento individualmente:
# através do "Beautufulsoup podemos acessar cada tag dentro do html"
# 'html.parser' estrutura da pagina html, poderia ser também 'lxml'.
soup = BeautifulSoup(resposta.text, 'html.parser')
# "prettify" significa embelezar, vai mostrar a estrutura da página html com a identação.
print(soup.prettify())