def linha(tam=30):
    print('-' * tam)



def cabecalho(msg):
    linha(40)
    print(msg)
    linha(40)


def numInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except(TypeError, ValueError):
            print('\033[31m[ERRO] digite apenas números!\033[m')
        else:
            return n


def verifArq(nome):
    try:
        with open(nome, 'r') as f:
            nome = f.read()
    except FileNotFoundError:
        return False
    else:
        return True


# Função para verificar se o arquivo existe. (.txt)
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')# Verificando se um arquivo existe.
        a.close() # Fecha o arquivo.
    except FileNotFoundError:
        return False
    else:
        return True
#-------------------------


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')# Método 'wt+' serve para criar um arquivo.
        a.close() # Fecha o arquivo.
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')




from time import sleep


cont = 0

logins = [2244, 1122, 3344]
while True:
    cabecalho('ACADEMIA FIT'.center(40))
    senha = numInteiro('Senha: ')

    while senha not in logins:
        print('SENHA INVÁLIDA!')
        senha = numInteiro('Senha: ')
    if senha in logins:
        print('(A)- Cadastrar Alunos | (B) - Ver Alunos Cadastrados | (C) - Analisar IMC')
        print('\033[34mBem Vindo(a)\033[m'.center(48))
        sleep(2)
        desejo = str(input('O que deseja fazer? ')).upper()
        while desejo not in 'abc'.upper():
            print('Opção inválida!')
            print('(A)- Ver Alunos Cadastrados | (B) - Cadastrar um Novo Aluno | (C) - Criar um Arquivo | (D) - Analisar o IMC')
            desejo = str(input('O que deseja fazer? ')).upper()
        if desejo == 'a'.upper():
            if not arquivoExiste('myfile.txt'):
                criarArquivo('myfile.txt')
            else:
                print('O Arquivo já Existe!')










