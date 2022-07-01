from arquivos import *

def cabecalho(txt):
    linha()
    cabecalho = print(txt)
    linha()
    return cabecalho


def linha(tam=40):
    print('-' * tam)


def leiaInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except(TypeError, ValueError):
            print('ERRO: Digite um inteiro válido')
        else:
            return n



def leiaStr(txt):
    while True:
        n = str(input(txt))
        if n.isnumeric() == True:
            print('ERRO: Digite Seu Nome: ')
        else:
            return n






def menu():
    print('\033[35m1 - Ver Pessoas Cadastradas \n2 - Cadastrar uma Nova Pessoas \n3 - Sair do Programa \n4 - Apagar um registro\033[m')









