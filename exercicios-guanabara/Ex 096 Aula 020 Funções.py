# Faça um programa que tenha uma função chamada área(), que eceba dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno.

'''def Linha():
    print('-' * 30)


def area(largura, comprimento):
    mult = largura * comprimento
    print(f'A área de um terreno com {largura}X {comprimento} é de {mult}')


Linha()
print('CONTROLE DE TERRENO')
Linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
'''


def area(larg, comp):
    a = larg * comp
    print(f'A área do terreno de {larg} por {comp} é {a}')


l = float(input('Qual a largura do terreno? (M) '))
c = float(input('Qual o comprimento do terreno: (M) '))
area(l, c)


