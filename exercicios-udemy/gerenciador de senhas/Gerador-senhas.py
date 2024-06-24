import string # para usar ascii_letters
import time
from random import choice
from time import sleep




def centralizar():
    frase = 'GERADOR DE SENHAS'
    fr = frase.center(40)
    print(fr)
    print()



def apenas_numeros(nume):
    while True:
        try:
            num = int(input(nume))
        except ValueError:
            print('ERRO (digite apenas números)')
        else:
            print(num)
            break



def gerador_senha():
    centralizar()
    sleep(2)
    while True:
        proibida = ['n', 'N', 'S', 's']
        try:
            tam_senha = int(input('Digite o tamanho da sua senha? [digite 0(zero) para sair)] '))
            if tam_senha == 0:
                print('Saindo...')
                sleep(2)
                break
        except ValueError:
            print('ERRO (digite apenas números!) ')
        else:
            caracteres = string.ascii_letters + string.digits + string.punctuation
            senha_segura = ''
            for c in range(tam_senha):
                senha_segura += choice(caracteres)
            print(f'A senha gerada foi: {senha_segura}')
            sleep(2)
            print()
            desejo = str(input('Deseja continar gerando senhas? [S para Sim ou N Para Não] '))
            print()
            if desejo == 's' or desejo == 'S':
                continue
            elif desejo == 'n' or desejo == 'N':
                break
            while desejo not in proibida:
                print('ERRO! (digite S para Sim ou N para Não)')
                desejo = str(input('Deseja continar gerando senhas? [S para Sim ou N Para Não]'))
            if desejo == 'n':
                break


gerador_senha()