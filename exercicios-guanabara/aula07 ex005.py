from time import sleep
azul = '\033[36m'
vermelho = '\033[31m'
n1 = int(input('Digite um número:'))
print('O número digitado foi {}'.format(n1))
s = n1 +1
a = n1 -1
print('carregando...')
sleep(3)
print('Seu sucessor é {}'.format(s))
print('Seu antecessor é {}'.format(a))

