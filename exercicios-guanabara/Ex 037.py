#Ex 037
'''Escreva um programa que leia um número inteiro qulaquer e peça para o usuário escolher qual será a base de conversão:

-1 Pra binário
-1 Para octal
-3 Para hexadecimal'''

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('sua opção:'))
if opção == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} concertido em HEXADECIMAL é igual a {}'.format(n , hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente.')

