from interface import *
from arquivos import *
from time import sleep

arquivo = 'pessoas.txt'
if not existenciaArq(arquivo):
    criandoArquivo(arquivo)
while True:
    cabecalho('CADASTRO DE PESSOAS'.center(40))
    menu()
    linha()
    resposta = leiaInteiro('O que deseja fazer? ')
    linha()
    if resposta == 1:
        lerAquivos(arquivo)
        sleep(2)
    elif resposta == 2:
        nome = leiaStr('Nome [\033[37mPressione N para Cancelar]: \033[m').capitalize().strip()
        if nome in 'N'[0]:
            break
        num = leiaInteiro('CPF: ')
        cadastrarArq(arquivo, nome, num)
        sleep(2)
    elif resposta == 3:
        print('Saindo do programa...')
        sleep(2)
        break
    elif resposta == 4:
        nome = leiaStr('Registro a ser apagado: ').capitalize()
        a = open(arquivo, 'w+')  # Essa linha apaga todos os arquivos salvos em txt.
        a.close()
    else:
        print('Opção inválida!')
        sleep(1)








