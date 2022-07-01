from pythonexercicios.programando.programando2.meucodigo import *

logins = [2244, 1122, 3344]
while True:
    cabecalho('ACADEMIA FIT'.center(40))
    senha = numInteiro('Senha: ')
    print()
    if senha in logins:
        print('Seja Bem Vindo(a)!'.center(40))
        break
    print()
    print('(A)- Cadastrar Alunos | (B) - Ver Alunos Cadastrados | (C) - Analisar IMC')

