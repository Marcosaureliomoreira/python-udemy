
def leiaInteiro(txt):
    while True:
        try:
            n = int(input(txt))
        except (TypeError, ValueError):
            print('\033[31mERRO! digite apenas números.\033[m')
        else:
            return n


def linha(tam=40):
    print('=' * tam)

def cabecalho(frase):
    linha()
    print(frase)
    linha()



def miniBancodados():
    from datetime import date, datetime
    cod = leiaInteiro('Sua Senha: ')
    if cod == 1111 and 18 <= hora_atual < 24:
        print('Bem vindo MARCOS!')
        print('Boa Noite!')
        print(dataformatada)
    elif cod == 1111 and 6:
        print('Bem vindo Marcos')
    elif cod == 2222:
        print('Bem vinda KAMILA')
        print(dataformatada)
    elif cod == 3333:
        print('Bem vinda SUELLEN')
        print(dataformatada)
    else:
        print('Inválido!')



from datetime import date, datetime
from time import sleep
hora_atual = datetime.now().hour
cabecalho('\033[36mSISTEMA DE PONTO\033[m'.center(45))
data = datetime.today()
dataformatada = data.strftime('%d/%m/%Y \t\t%H:%M:%S')
print(dataformatada)
miniBancodados()


