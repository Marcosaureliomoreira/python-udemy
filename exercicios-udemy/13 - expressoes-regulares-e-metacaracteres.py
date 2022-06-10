import re # Regular expression ou regex

padrao = re.compile('abc')

m = padrao.match('abcd abc')   # Vai procurar por padrão 'abc' e se encontrar vai imprimir.
#print(m.group())

m = padrao.search('bcd abc')  # Utilizando o método "search" vai retornar o valor "abc" mesmo se não estiver nessa ordem.
#print(m.group())

m = padrao.findall('abcd abc') # "findall" Este padrão exibe todos os padrões de texto dentro de uma lista. diferente do "match".
#print(m) # para utilizar o findall não podemos usar a variável padrao, apenas imprimir direto.




def encontrar(regex, texto, opcao = 'match'):
    """opcao ==> match, search ou findall"""
    p = re.compile(regex)  # "p" é de padrao
    m = p.__getattribute__(opcao)(texto) # Modificando o atributo, em opcao podemos colocar "match, findall ou search".
    if m:
        if opcao != 'findall':
            return print(m.group())
        return print(m)


#encontrar('abc', 'abcd abc', 'findall')

#=======================================================================================================================
                                        # Metacaracteres

'''print('.^ $ * + ? { } [ ] \ | ( )')
regex = '[a-c]+' # Do "a" até o "c"
texto = 'abcd abc Significa Caracteres do a até o c' # Vai encontrar todos que tiverem a letra a e c e ambas juntas.
#encontrar(regex, texto, 'findall')'''




'''regex = '[a-zA-Zà-ùÀ-Ù]+'  # è preciso colocar crases nas letras para receberem acentuação.
texto = 'É preciso adicionar à-ù para detectar acentuação para letras minúsculas' # Vai encontrar todos que tiverema a letra a e c e ambas juntas.
encontrar(regex, texto, 'findall')'''



#PARA DETECTAR NÚMEROS:

'''regex = '[0-9]+' 
texto = '0-9 pra detectar números como 13, 18 e 7, \ só estou colocando números aleatórios' # Detectando números
encontrar(regex, texto, 'findall')'''


#NEGAÇÃO:

'''regex = '[^0-9]+' # Depois do sinal de negação "^" Tudo que estiver depois será negado.
texto = '0-9 pra detectar números como 13, 18 e 7, só estou colocando números aleatórios' # Detectando números
encontrar(regex, texto, 'findall')'''

#=======================================================================================================================
                                        #Metacaracteres parte2

'''regex = '[a-zA-Z_]+' # sem o sinal de mais "+", iria mostrar letra por letra
texto = 'O preço é $200 palavra_junta'
encontrar(regex, texto, 'findall')'''


# Utilizando o caracteres colchete dentro de colchete:

'''regex = '[a-zA-Z0-9$_\[\]]+' # Temos que utilizar a contra barra para poder usar o caractere colchete dentro de colchetes.
texto = 'O preço é $200 palavra_junta'
encontrar(regex, texto, 'findall')'''

#=======================================================================================================================
                                        # SEQUÊNCIAS ESPECIAIS

# \d : qualquer digito de [0-9].
# \D : qualquer caractere não digito [^0-9].
# s : qualquer caractere espaço em branco [\t\n\r\f\v].
# \S : qualquer caractere não-espaço-branco [^\t\n\r\f\v].
# \w : qualquer caractere alfanúmérico [a-zA-Zà-ùÀ-Ù0-9_].
# \W : qualquer carectera não-alfanumérico [^a-zA-Zà-ùÀ-Ù0-9_].



'''regex = '[\d$]+' # Temos que utilizar a contra barra para poder usar o caractere colchete dentro de colchetes.
texto = 'O preço é $200 palavra_junta'
#encontrar(regex, texto, 'findall')'''
#=======================================================================================================================
                                        #String crua(Raw string)

#print(r'\tTAb \nPulando linha')
#Colocando o "r" no começo da frase, dizemos ao pc que não queremos fazer nada e assim teremos a string crua.
#=======================================================================================================================
                                        #.(Ponto)

# O .(ponto) faz um match com qualquer caracter.

'''regex = r'\.'
texto = 'exemplo de site.com ou email.com'  # Vai encontrar os .(pontos contidos no texto) 
encontrar(regex, texto, 'findall')'''


'''regex = r'\w+\.com'
texto = 'exemplo de site.com ou email eu@gmail.com'  # Vai encontrar os .(vai detectar as palavras terminadas em .com)
encontrar(regex, texto, 'findall')'''


'''regex = r'\w+\.com'
texto = 'exemplo de site.com ou email eu@gmail.com'  # Vai encontrar os .(vai detectar as palavras terminadas em .com)
encontrar(regex, texto, 'findall')'''
#=======================================================================================================================

                                        #SEQUÊNCIA ESPECIAL \b e \B

'''regex = r'ta\b'     # Para pegar o final da palavra.
texto = 'tampa a panela Roberta Batata'  
#encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m)'''



'''regex = r'ta\B'   # Para pegar o começo da palavra. vai pegar o "ta" da palavra tampa.
texto = 'tampa a panela Roberta Batata'
#encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m)'''

#-----------------------------------------------------------------------------------------------------------------------

                                            #Pipe - ou
                                    # A|B A ou B uma coisa ou outra.

'''regex = r'ta\B|TA\B'   # Vai pegar o o "ta" maíusculo ou minúsculo para isso utilizamos o operador ou "|".
texto = 'Tampa a panela Roberta Batata'
#encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m)'''




'''regex = r'eu@(gmail.com |hotmail.com)'   # Nesta linha temos um grupo.
texto = 'eu@gmail.com e eu@hotmail.com'
#encontrar(regex, texto, 'findall')
p = re.compile(regex)
matches = p.finditer(texto)
for m in matches:
    print(m.group())'''
#=======================================================================================================================

                                        #Circunflexo e $ Sifrão

'''regex = r'^Começo' # vai pegar a palavra começo, referente a frase abaixo.
texto = 'Começo de uma frase. Agora vou escrever o final.'
encontrar(regex, texto, 'findall')'''




'''regex = r'final$' # Com o $ pegamos a palavra do final.
texto = 'Começo de uma frase. Agora vou escrever o final'
encontrar(regex, texto, 'findall')'''

#=======================================================================================================================

                                # Número exato de cópias

'''regex = r'\d{5}-\d{4}' # Vai pegar os números de telefones.
texto = 'Telefones 99874-6854, 9984.5486, 965473214'
encontrar(regex, texto, 'findall')


regex = r'\d{5}[-.]?\d{4}' #Vai pegar os números mesmo se estiverem separados por .(ponto), -(traço), ou tudo junto(?)
texto = 'Telefones 99874-6854, 9984.5486, 965473214'
encontrar(regex, texto, 'findall')'''
#=======================================================================================================================

                                # * (asterisco) de 0 a multos

'''regex = r'Dra?\.*' #  Com o asterisco conseguimos pegar todos os elementos, diferente do "?" que pega "um" ou "nenhum".
texto = """
Titulos
Dr Gato
Dr. Pato
Dra.. Pata
Dra Raposa
"""
encontrar(regex, texto, 'findall')'''
#=======================================================================================================================

                                     # COLCHETES[]
                    # Range de catacteres ou caracteres escíficos

'''regex = r'\d+[-.*]?\d+' #Vai pegar os números mesmo se estiverem separados por .(ponto), -(traço), ou tudo junto(?) ou astarisco.
texto = 'Telefones 99874-6854, 9984*5486, 965473214'
encontrar(regex, texto, 'findall')



regex = r'[a-fA-F0-2-T-l]' # Fazendo o match com o range e pegando caracteres do texto. se colocarmos o "+" no final, juntamos os caracteres.
texto = 'Telefones 99874-6854, 9984*5486, 965473214'
encontrar(regex, texto, 'findall')'''

#=======================================================================================================================

                                    # [^] exceto os caracteres dentro de colchetes

'''regex = r'[^r]ato' # Não vai entrar a palavra "rato" pq colocamos o exceto[^r] entre colchetes.
texto = 'Gato pato rato'
encontrar(regex, texto, 'findall')'''
#-=====================================================================================================================
                                    # GRUPOS ()

'''regex = r'(\w+)\.' # Dessa meneira, com o "w+" entre parêntese pegamos o "Dr" mas não pegamos o ponto,
texto = """
Títulos
Dr. Gato
Dr. Pato
Dra. Pata
Dra. Raposa
"""
encontrar(regex, texto, 'findall')


p = re.compile(regex)
matches = p.finditer(texto)  #Fazendo sem a função, usando o "finditer"
for m in matches:
    print(m.group(1))'''



'''regex = r'eu@(gmail|yahoo|hotmail).com'
texto = """
eu@gmail.com
eu@yahoo.com
eu@hotmail.com
"""
#encontrar(regex, texto, 'findall')

p = re.compile(regex)
matches = p.finditer(texto)  #Fazendo sem a função, usando o "finditer"
for m in matches:
    print(m.group())  #O indíce "1" que esta entre parênteses significa o segundo grupo, a frase completa.'''

#------------------------------------------------------------------------------------------------------------------------
                                            # {m,n} Ranges de números e repetições

                    # {m,n} >>> range de números e repetições
                    # {0,1} >>> ?0 ou uma repetição
                    # {1,} >>> +pelo menos uma
                    # {0,} >>> *nenhuma ou mais


'''regex = r'\w{0,}'  # Vai pegar tudo que estiver no texto (de zero a muitos) é a mesma coisa que colocar um *
texto = """
a
ab
abc
abcdefg
oadsogjdjfg
"""

encontrar(regex, texto, 'findall')





regex = r'\w{1,}'  # Vai pegar somente os caracteres do tipo "w" que são do tipo alfa numérico e não vai entrar os enters e os espaços em branco como acima. é a mesma coisa que "\w+"
texto = """
a
ab
abc
abcdefg
oadsogjdjfg
"""

encontrar(regex, texto, 'findall')






regex = r'\w?'  # é a mesma coisa que {0, 1} zero ou um.
texto = """
a
ab
abc
abcdefg
oadsogjdjfg
"""

encontrar(regex, texto, 'findall')







regex = r'\w{2,3}\n' # vai pegar somente a palavra iniciando nos dois primeiros caracteres.
texto = """
a
ab
abc
abcdefg
oadsogjdjfg
"""

encontrar(regex, texto, 'findall')







regex = r'\w{2,3}' # vai pegar as palavras separadas por espaços. se coloco parêntese entre o regex "r'(\w{2,3}) '" significa um grupo em específico e pego as palavras sem os espaços.
texto = """
a ab abc abcdefg oadsogjdjfg 
"""

encontrar(regex, texto, 'findall')'''

#-----------------------------------------------------------------------------------------------------------------------

                                    #Exercício: Identificando padrões de Emails

#OBS: para pegar - (traços), * (asteriscos) e outros caracteres especiais temos que especifica-los dentro de [](colchetes).

'''regex = r'[\w-]+@[\w-]+\.\w+' #Vai pegar todos os emails, com todos os caracteres especiais.
texto = """
Texto antes
ga_to@gmail.com
pa-to@yahoo.com
No meio alguns textos
pata1995@meu-email.edu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""
encontrar(regex, texto, 'findall')







regex = r'[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+\.\w+' #Teremos o mesmo resultado que a expressão acima, porém não aceitará acentuação no email.
texto = """
Texto antes
ga_to@gmail.com
pa-to@yahoo.com
No meio alguns textos
pata1995@meu-email.edu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""
encontrar(regex, texto, 'findall')






regex = r'([a-zA-Z0-9-_]+)@([a-zA-Z0-9-_]+)\.(\w+)' # Neste exemplo conseguimos pegar todos os emails de forma literal.
texto = """
Texto antes
ga_to@gmail.com
pa-to@yahoo.com
No meio alguns textos
pata1995@meu-email.edu
rato2020@hotmail.com
k@email.net
E depois alguns textos
"""
#encontrar(regex, texto, 'findall')

p = re.compile(regex)
matches = p.finditer(texto)  #Fazendo sem a função, usando o "finditer"
for m in matches:
    print(m.group(3))  # Aqui pegamos o grupo, se deixarmos sem nada entre parêntese pego todos, se especificar-mos, por número ele pegará determinado grupo.
'''
#-----------------------------------------------------------------------------------------------------------------------

                                #Exercício: Identificando Padrões de Sites



regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?' # O ponto de interrogação significa que o "s" é opcional. O \.(contrabarraponto) significa que o vai fazer o match a partir do .(ponto)
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
#for m in matches:
    #print(m.group(2))


                                # Substituição de Strings(continuação)

#sites_normalizados = p.sub(r'https://www.\2.\3\4', texto) #Vai substituir o resto do texto mostrando só o grupo 2.
#print(sites_normalizados)


'''#"sub" é o método para subsrituir.

#entre parêntese temos a "expressão regular" e ao lado a variável "texto" que é o texto contido nela que vai ser modificado.

# \2.\3\4 são grupos dentro do texto.

# O "https://www." são as iniciais do texto'''

#-----------------------------------------------------------------------------------------------------------------------

                            #Métodos match, search e finditer

regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?' # O ponto de interrogação significa que o "s" é opcional. O \.(contrabarraponto) significa que o vai fazer o match a partir do .(ponto)
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
match = p.match(texto)
if match:
    print(match.group())
else:
    print(match)
'''Vai imprimir None pq o match só pega o texto se estiver no começo e o primeiro no texto são trÊs aspas duplas.'''








#Search:

regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?'
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
match = p.search(texto)
if match:
    print(match.group())
else:
    print(match)
'''Vai imprimir o primeiro site que ele encontrar'''








#Findall(encontrar todos)
regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?' # O ponto de interrogação significa que o "s" é opcional. O \.(contrabarraponto) significa que o vai fazer o match a partir do .(ponto)
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
lista_matches = p.findall(texto)
print(lista_matches)
'''Mostra todos os itens encontrados'''










#finditer(gera iteradores)

regex = r'https?://(www\.)?(\w+)\.(com|net|org)(\.\w+)?' # O ponto de interrogação significa que o "s" é opcional. O \.(contrabarraponto) significa que o vai fazer o match a partir do .(ponto)
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
m = p.finditer(texto)
#print(next(m))    # "next" significa que vai imprimir um de cada vez até chagar no último.
for match in m:
    print(match.group())

