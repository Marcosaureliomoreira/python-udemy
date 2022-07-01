from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')# Verificando se um arquivo existe.
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')# Método 'wt+' serve para criar um arquivo.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')# método 'rt' serve para ler um arquivo.
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()



def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')# O método 'at' vem de append, que é adicionar elementos.
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}: {idade}\n')
        except:
            print('Houve um ERRo na hora de escrever os dados!')
        else:
            print(f'Novo registro: {nome} adicionado.')
            a.close()




