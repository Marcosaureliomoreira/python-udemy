"""
Para criar a uma aplicaçãa web com flask, temos que acessar o ambiente virtual do Pycharm, que é a pasta chamada "venv"
a lá podemos criar um novo arquivo python para ser a aplicação, Logo a seguir acessar a pasta pelo terminal, se quesermos ver
os pré-requisitos para rodar a aplicação, podemos dar o comando "pip freze". Para rodar no navegador temos que dar alguns
comandos dentro do arquivo que criamos, arquivos estes da biblioteca "flask" e depois no termminal dar o comando "python + nome da aplicação"
Exemplo: python app.py. Logo a seguir copiar a caminhor que vai ser gerado, copiar e colar no navegador para poder acessar a aplicaçõ, de uma
forma local.
#-----------------------------------------------------------------------------------------------------------------------

Gerando e instalando módulos via requiriments.txt:
Para compartilhar outras pessoas.

-Dentro da pasta venv que é p ambiente virtual
-Digitar no terminal o comando: pip freeze > requirements.txt
-Depois de requiriment.txt for criado, ainda no terminal digitar: pip install -r requirements.txt
para instalar as bibliotecas.
-Depois podemos podemos inciar a aplicação pelo nome para ver se esta funcionado exemplo: python app.py
-Estando tudo ok, podemos dar o comando: flask run
-Depois dar um flask run --host=0.0.0.0 para ele rodar como público e aceitar qualquer requisição externa. (funciona como localhost)
podeira até escolher um ip.

CRIANDO E RENDERIZANDO PÁGINAS HTML:

- Para rodar a aplicação podemos dar no terminal o comando: flask run ou com python + nome do arquivo.py
exemplo: python.app
-Na pasta do ambiente virtual(venv) crias as pastas templates e static que fará parte do ambiente virtual.
-O flask vai procurar dentro da para templates por arquivos HTML e através desses arquivos ele var renderizar.
-Dentro da pasta templates, criar um arquivo html, exemplo: site.html, e escrever a estrutura básica da página html.
-depois do código HTML criado, basta ir na aplicação que será rodada e ao lado de da importação do flask, importar o
render_template EXEMPLO: from flask import Flask, render_template. que vai fazer a importação do arquivo HTML que está
dentro da pasta "template"
- Depois disso ir na aplicação a ser rodada e na função index, em "return' colocar o "render_template" que á a pasta que
será retornado para o site.
-Depois disso é só rodar ou dar um CTRL+C para interremper a aplicação e rodar novamente.

APLICANDO CSS NO SITE:
-ainda na página html, criamos um link com o caminho: <link rel="stylesheet" href="../static/style.css">
ou seja: href="../static/style.css" significa que estamos saindo da pasta principal de HTML e entrando em:
static que var ser o estilo css.

"""