from interface import *

def existenciaArq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True


def criandoArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerAquivos(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        print(a.read())
    finally:
        a.close()



def cadastrarArq(arquivo, nome='desconhecido', cpf=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'Nome: {nome.capitalize()} \nCPF: {cpf}\n\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro: {nome.capitalize()} adicionado com sucesso.')
            a.close()


#a.write(f'\nNome: {nome}: \nCPF: {cpf}')
# a = open(arquivo, 'w') # Essa linha apaga todos os arquivos salvos em txt.
        #a.close()





def apagar(nome):
    try:
        a = open(nome, 'w')
    except:
        print('Houve um ERRO na tentativa de ler o arquivo.')
    else:
        print(f'Registro {nome} apagado com sucesso.')
        a.close()



def apagararq(nome, arq):
    if nome in arq:
        a = open(nome, 'w')
        a.close()
        print('Registro apagado')
    else:
        print('Arquivo inexistente.')

