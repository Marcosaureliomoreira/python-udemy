#Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

'''from time import sleep
multiplicação = 0
escolha = 0


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
while escolha != 5:
    print('\n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
    escolha = int(input('O que deseja?'.format(escolha)))

    if escolha == 1:
        soma = n1 + n2
        print('Você optou por somar e a soma de {} + {} é {}'.format(n1, n2, soma))
    elif escolha == 2:
        multiplicação = n1 * n2
        print('Você optou por multiplicar e o resultado dos números {} X {}  é {}'.format(n1, n2, multiplicação))
    elif escolha == 3:
        if n1 >  n2:
            print('O primeiro número é MAIOR!')
        if n2 > n1:
            print('O segundo número é MAIOR')
        else:
            print('Os números são IGUAIS!')

    elif escolha == 4:
        print('Informe os novos valores: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')

    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')'''

































'''multiplicação = 0
escolha = 0
novosn = 0

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))

print('[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa')
escolha = int(input('O que deseja?'.format(escolha)))

if escolha == 1:
    soma = n1 + n2
    print('A soma dos números digitados é {}'.format(soma))
elif escolha == 2:
    multiplicação = n1 * n2
    print('O resultado dos números multiplicados é {}'.format(multiplicação))
elif escolha == 3:
    if n1 >  n2:
        print('O primeiro número é MAIOR!')
    if n2 > n1:
        print('O segundo número é MAIOR')
    else:
        print('Os números são IGUAIS!')

while escolha == 4:
    novosn = int(input('Digite NOVOS números:'.format(novosn)))'''


















