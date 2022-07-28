# WEB SCRAPING é coletar informações na web, baseado na estrutura do site.

"""
- Uma das formas de saber se o site permite o uso de "web scraping" é digitar no buscador:
com o final /robots.txt.
EXEMPLO: google.com/robots.txt

- Já dentro da página que vai aparecer com informações de permissões de uso do site, verificar se
o "User-agent" esta com o sinal de * (asterisco) que significa todos.
EXEMPLO: User-agent: *
Caso esteja, significa que o site permite o uso de webscraping para coletar informações. Do ao contrário
pode gerar implicações.

- O site também permitir somente algum/alguem filtrar informações, neste caso o user-agent será específico.
EXEMPLO: User-agent: applebot
ou seja somente esse applebot terá acesso.

allow: são as páginas/caminhos permitidas.
disallow: são as páginas/caminhos não permitidos

"""