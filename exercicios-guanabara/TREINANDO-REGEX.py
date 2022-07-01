import re


def encontrar(regex, texto, opcao ='match'):
    p = re.compile(regex)
    m = p.__getattribute__(opcao)(texto)
    if m:
        if opcao != 'findall':
            return print(m.group())
        return print(m)


'''regex = 'r[a-z-A-Z-c-ç-à-ù-0-9]+'
texto = 'O preço é $ 200'
encontrar(regex, texto, 'findall')
for palavra in texto:
    palavra.replace("''", " ")
    print(palavra, end='')'''
#----------------------------------------------------------------------------------------------------------------------


#EXERCÍCIO PARA IDENTIFICAR SITES DENTRO DE UM TEXTO:
'''regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?' # O ponto de interrogação significa que o "s" é opcional. O \.(contrabarraponto) significa que o vai fazer o match a partir do .(ponto)
texto = """
Sites
https://www.meusite.com
http://outrosite.net
http://google.com
https://www.site.org
http://sitebrasileiro.com.br
"""
#encontrar(regex, texto, 'findall')

p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m.group())

sites_normais = p.sub(r'https://www.\2.\3\4', texto)
print(sites_normais)'''

#-----------------------------------------------------------------------------------------------------------------------




'''def regex(n):
    t = re.compile(r'[\w-]+@[\w.]+')
    m = t.findall(n)
    if m:
        for l in m:
            print(l)
    elif m == []:
        print('Não há resultados!')



regex("""
Este texto possui
marcos_230@gmail.com
ad-meuemail@hotmail.com
adriana-meni@.net
Fim do Texto.
""")'''

'''def expressao_reg(n):
    e = re.compile(r'[^\w+]+')
    f = e.findall(n)
    for l in f:
        print(l, end=' ')



expressao_reg("""
Hoje está um día muito boníto! @
""")'''



def exprReg(txt):
    e = re.compile(r'')
    f = e.findall(txt)
    for l in f:
        print(l, end=' ')


n = exprReg("""
Mercos Aurelio
""")


















