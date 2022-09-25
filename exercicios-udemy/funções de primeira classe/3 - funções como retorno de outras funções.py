# Funções como retorno de outras funções

def mensageiro(mensagem):
    def print_mensagem():
        print(mensagem)
    return print_mensagem


diz_ola = mensageiro('Olá!')
diz_ola()

diz_oi = mensageiro('Oi')
diz_oi()


# Outros exemplos:
# fazendo uma função que formata texto e tendo como resultado outra função com o texto formatado

def tag_html(tag):
    def formata_texto(mensagem):
        print(f'<{tag}>{mensagem}</{tag}>')
    return formata_texto

# exeplo 1:
h1 = tag_html('h1')
h1('Meu Titulo HTML')


# exemplo 2:
p = tag_html('p')
p('Meu primeiro parágrafo')

