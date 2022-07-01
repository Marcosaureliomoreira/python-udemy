#Aula 011: CORES NO TERMNAL
#Código das cores, padrão ANCI

'''\033[0:30:41m  #Fundo vermelho e letra branca
\033[4:33:44m  #fundo azul e letra amarela
\033[1:35:43m  #Fundo amarelo e letra roxa
\033[30:42m    #Fundo verde com letras brancas
\033[m         #Fundo preto com letras brancas
\033[7:30m     #Findo branco com letra preta'''

#print('\033[4;30;43mOlá mundo!\033[m')

'''a = 3
b = 5
print('Os valores são \033[33m{} e \033[34m{}'.format(a, b))'''


nome = 'Marcos'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))