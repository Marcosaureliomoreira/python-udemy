#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um
#arquivo de texto simples. O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        #Opção de listar o contúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[32mSaindo do sistema...Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)



