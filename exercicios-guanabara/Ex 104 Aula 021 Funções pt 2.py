#Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante a função input do python, só que fazendo a validação,
# para aceitar apenas valor numérico.
# EXEMPLO: n = intinput('Digite um número n')



def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Programa principal
n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
















