"""
# Fazendo com o site imdb.com
# Acessando a lista de 250 filmes masi assistidos
# Caminho da página dos filmes mais assistidos: https://www.imdb.com/chart/top/?ref_=nv_mv_250


1 - Acessar o site imdb.com
2 - Acessar o prompt de comando, pelo pycharm mesmo
3 - Acessar o ambiente virtual (venv) e criar uma pasta.
4 - Depois de criado, acessar essa pasta.
5 - Instalar o scrapy pelo prompt: pip install "scrapy"
6 - Dentro da pasta criada no ambiente virtual no meu cas0 filmesImdb:
digitar os camndo: "scrapy startproject imdb250, para criar um projeto chamado imdb250
mas que pode ser outro nome.
7 - Depois de criado basta acessar com o comando cd.
8 - Uma vez dentro da pasta, digitar o comando: "scrapy genspider imdb imdb.com"
(Para criar um imdb.py dentro do ambiente virtual e ele virá com algumas informações.)
9 - "scrapy shell" é o ambiente de testes do scrapy, podemos testar nossos códigos.
10 - basta acessar pelo terminal: scrapy shell. Quando acessado o terminal mudará o caminho
para três setas(>>>) indicando que estamos no ambiente de testes do scrapy.
11 - Para testar temos que digitar o comando "fetch()" com o endereço do site para testarmos
a conexão. Exemplo: fetch('https://www.imdb.com/chart/top/?ref_=nv_mv_250') e dar enter.
se aparecer como resposta (200), significa que esta ok e a conexão foi feita.

*Instalar a extensão do chrome "selectorGadget" para filtrar informações para usar no scrapy.Ele
permite fazer tudo o que o inspecionar fazia.

12 - Com essa extensão podemos pegar as informações dos filmes, basta clicar apenas encima da
extensão e e depois clicar no link correspondente ao que queremos pegar informações e copiar da caixinha
da extensão que fica no rodapé da página. e podemos até guardar as informações no bloco de notas,para depois
usarmos.
-----------------------------------------------------------------------------------------------------------
13 - Para obtermos uma resposta da caixa com o nome do filme temos que: dar o comando:
response.css('.titleColumn').get() para pegarmos a informação do primeiro item(filme).
Para pegar a lista completa temos que passar o: response.css('.titleColumn').getall()

14 - Podemos colocar esse conteúdo dentro de uma variável. Exemplo:
filmes = response.css('.titleColumn')
* A partir daí podemos acessar como se fosse uma lista. Exemplo:
filmes[15] - Vai acessar o filme da posição 15.
len(filmes) - Vai mostrar a quantidade de filmes dentro da variável.

15 - Depois posso jogar essa variável filmes que está recebendo o código css dentro da função parse,
quando formos rodar a função, fora do shell, que é o teste.
Exemplo:
    def parse(self, response):
        filmes = response.css('.titleColumn')
        pass
-----------------------------------------------------------------------------------------------------------------
16 - Para pegar o nome do primeiro filme dos mais assistidos do site indb: response.css('.titleColumn a').get()
- Para pegar todos: response.css('.titleColumn a').getall()
- Adicionando dentro de uma variável: tutulo = response.css('.titleColumn a')
- Acessando através de indices:
len(filmes)
filme[10]

* Depois que ver que está funcionando posso colocar a variável que recebe os dados, na funçõo "parse"
para rodar for do shell, que é para teste

-------------------------------------------------------------------------------------------------------------

17 - Para pegar apenas o nome do primeiro filme: response.css('.titleColumn a::text').get()
18 - Para pegar apenas o nome de todos os filmes: response.css('.titleColumn a::text').getall()
- Acessando através de indices:
len(titulos)

titulos = response.css('.titleColumn a::text')   << será adicionada na função "parse"

* Depois que ver que está funcionando posso colocar a variável que recebe os dados, na funçõo "parse"
para rodar for do shell, que é para teste

-------------------------------------------------------------------------------------------------------------
19 - Para pegar o ano do filme que está na primeira linha do site: response.css('.secondaryInfo').get()
20 - Para pegar o ano de todos os filmes que está na lista dos mais assistidos do site:
response.css('.secondaryInfo').getall()
21 - Para pegar somente o ano dos filmes: response.css('.secondaryInfo::text').getall()
22 - adionando em uma variavel:
anos = response.css('.secondaryInfo::text')
acessando por indices:
len(anos)

* Depois que ver que está funcionando posso colocar a variável que recebe os dados, na funçõo "parse"
para rodar for do shell, que é para teste
------------------------------------------------------------------------------------------------------

23 - Pegar a avaliação do filme: response.css('strong').get()
- Pegar somente a avaliação(sem caracteres especiais):
response.css('strong').get()
- Pegar somente a avaliação dos filmes(sem caracteres especiais):
response.css('strong::text').getall()
- Adicionando a uma variavel:
nota = response.css('strong::text')
- Aceessando por indices:
len(notas)

* Depois que ver que está funcionando posso colocar a variável que recebe os dados, na funçõo "parse"
para rodar for do shell, que é para teste
--------------------------------------------------------------------------------------------------------------

QUANDO TERMINADO ESSA ETAPA DO SHELL, POSSO SAIR DO SHELL COM O COMANDO: quit()

IMPORTANTE:
Para rodar o spyder com o programa para pegar as informações:
digitar no terminal(fora do ambiente de testes shell): scrapy crawl imdb e dar enter.
Lembrando que "imdb" é o nome que dei ao programa.

IMPORTANTE:
Para rodar o programa e ao invés de ter as informações no terminal, posso jogar dentro de um
outro arquivo, por EXEMPLO, um json com o comando abaixo:

scrapy crawl imdb -O imdb.json

-Assim vai criar um arquivo json com as informações baixadas do scrapy.

IMPORTANTE:
Baixando informações e criando em arquivo CSV:

scrapy crawl imdb -O imdb.json

-Assim vai criar um arquivo CSV com as informações baixadas do scrapy.

"""

# Em "start_urls" no arquivo python, temos que colocar exatamente o endereço da página
# em que vamos fazer o scrapy.

# EXEMPLO: start_urls = ['https://www.imdb.com/chart/top/?ref_=nv_mv_250']


