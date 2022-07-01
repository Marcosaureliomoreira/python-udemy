'''n = int(input('Digite um número:'))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n,t,n,r))'''

dobro = 0
triplo = 0
raiz = 0
num = int(input('Digite um número:'))
print('\nMENU DE OPÇÕES:\n[2] para ver o dobro do número''\n[3] para ver o triplo \n[4] para raiz quadrada')
print('\nAnalise as opções acima e selecione a tecla correspondente.')
usuário = int(input('\nO que deseja fazer? '))
if usuário == 2:
    dobro = num * 2
    print('Você digitou o número {} e o seu dobro corresponde a {}'.format(num, dobro))
elif usuário == 3:
    triplo = num * 3
    print('Você digitou {} e o seu triplo corresponde a {}'.format(num, triplo))
elif usuário == 4:
    raiz = num ** (1/2)
    print('Voce digitou {} e sua raiz quadrada corresponde a {:.2f}'.format(num, raiz))
print('Você teclou {} no menu de opções.'.format(usuário))


















