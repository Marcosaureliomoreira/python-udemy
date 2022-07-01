#EX 040
'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
a media atingida:
-Média abaixo de 5.0:
REPROVADO
-Média entre 5.0 e 6.9:
RECUPERAÇÃO
Média 7.0 ou superior:
APROVADO'''
from time import sleep
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('AGUARDE!')
sleep(3)
print('A primeira nota foi:{} A segunda nota foi:{} e a sua media é:{}'.format(n1, n2, m))

if 7> m >= 5:    #MANEIRA CLAISSSICA DE SE FAZER: if média >= 5 and média < 7:
    print('O aluno esta em RECUPERAÇÃO')
elif m < 5:
    print('O aluno está REPROVADO')
elif m >= 7:
    print('O aluno está APROVADO.')

