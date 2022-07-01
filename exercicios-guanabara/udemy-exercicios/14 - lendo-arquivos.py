#Leitura de arquivos por linhas

#Jeito não recomendado
'''f = open('arquivo.txt', 'r') # r --> read (ler)
texto = f.read()
print(f.closed) # False
f.close()
print(f.closed) # True

print(texto)'''


#Jeito recomendado
# LENDO O TEXTO INTEIRO:

#Usando o método "with" o arquivo facha automaticamente.
'''with open('arquivo.txt', 'r') as f:
    texto = f.read() # O método "read()" ler todas as linhas do texto
    print(texto)
    print(f.closed) # False
print(f.closed) # True'''


# LENDO LINHA POR LINHA DO TEXTO:

'''with open('arquivo.txt', 'r') as f:  # este "f" é de arquivo, pode ser qualquer nome. "as" é um apelido.
    texto = f.readline() # O método "readline()" ler apanas a primeira linha do texto
    print(texto, end='')

    texto = f.readline() # Se executarmos novamente vai imprimir a segunda linha, e assim por diante.
    print(texto, end='')

    texto = f.readline()  # Se executarmos novamente vai imprimir a terceira linha, e assim por diante.
    print(texto, end='')'''


''' Por padrão o print sempre pula uma linha no final, para o próximo comando, para isso não contecer, temos que colocar o metodo
"end" print(texto, end) '''



#LENDO CADA LINHA DO TEXTO USANDO O "FOR":

'''with open('arquivo.txt', 'r') as f:
    for linha in f:
        print(linha, end='')'''
#=======================================================================================================================
                                   #LENDO ARQUIVOS POR CARACTERES


'''with open('arquivo.txt', 'r') as f:
    texto = f.read(80) # "f.read(80)" entre parentese podemos especificar a quantidade de caracteres a serem lidos
    print(texto)

    texto = f.read(80)  # "f.read(84)" Vai ler mais 84 caracteres além juntando com os 80 da linha acima.
    print(texto)'''




'''with open('arquivo.txt', 'r') as f:
    qtd = 10
    texto = f.read(qtd)
    while len(texto) > 0:
        print(texto, end='')
        texto = f.read(qtd)'''

#========================================================================================================================

                                #ESCREVENDO ARQUIVOS


#escrevendo no arquivo:
'''with open('arquivo.txt', 'w') as f: # "w" é de write - escrever
    f.write('Uma Frase qualquer\n')
    f.write('Uma segunda frase\n')'''




#Lendo o arquivo:
'''with open('arquivo.txt', 'r') as f: #Lendo o arquivo "r" de read - ler
    for linha in f:
        print(linha, end='')'''



#Adicionado arquivos:
'''with open('arquivo.txt', 'a') as f: # "a" é de append - adicionar, assim não apaga a linha anterior e sim adiciona.
    f.write('Uma quarta Frase\n')'''



'''with open('arquivo.txt', 'r') as f: #Lendo o arquivo "r" de read - ler
    for linha in f:
        print(linha, end='')'''







#Adicionando um texto externo:
'''texto = """
A Udemy é uma plataforma EAD, 
criada por Eren Bali, 
de e-learning para profissionais 
poderem tanto estudar como ensinar"""


#Escrevendo:
with open('udemy.txt', 'w') as f:
    f.write(texto)


#Lendo:
with open('udemy.txt', 'r') as f:
    for linha in f:
        print(linha, end='')


with open('udemy.txt', 'w') as f:
    f.write('Primeira linha\n')
    f.write(texto+'\n') #Concatenando texto com as linha que irão ser escritas.
    f.write('Última linha\n')


#Lendo:
with open('udemy.txt', 'r') as f:
    for linha in f:
        print(linha, end='')'''

#=======================================================================================================================

                            #CÓPIA DE ARQUIVOS DE TEXTO


#Copiando Arquivos:
'''with open('arquivo.txt', 'r') as meu_arq:
    with open('meu_arq_copia.txt', 'w') as meu_arq_copia:
        for linha in meu_arq:
            meu_arq_copia.write(linha)


#Lendo o Arquivo copiado:
with open('meu_arq_copia.txt', 'r') as f:
    for linha in f:
        print(linha, end='')'''













'''def abrirTexto(arq):
    with open('arquivo.txt', 'r') as a:
        arq = a.read()
        print(arq)

abrirTexto('arquivo.txt')'''
