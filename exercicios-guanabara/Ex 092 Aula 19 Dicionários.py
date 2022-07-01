#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em (com idade) em um dicionário,
# se por a caso a CTPS for diferente de zero, O dicionário receberá tambem o ano de contratação e o salário. Calcule
# e acrecente além da idade, com quantos anos a pessoa vai se aposentar.
'''from datetime import date
atual = date.today().year
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
pessoa['Idade'] = int(input('Nascimento: '))
pessoa['Idade'] = atual-pessoa['Idade']
pessoa['CTPS'] = int(input('Carteira e trabalho (0 não tem): '))
if pessoa['CTPS'] == 0:
    print('Carteira de trabalho (0 não possui)')
else:
    pessoa['ano contratação'] = int(input('Qual o ano de contratação: '))
    pessoa['salário'] = float(input('Qual o salário: '))
    pessoa['aposentadoria'] = pessoa['Idade'] + ((pessoa['ano contratação'] + 35) - atual)
print('-=' * 30)
for v, i in pessoa.items():
    print(f'{v}: {i}')'''




from datetime import datetime
trabalhador = dict()
trabalhador['nome'] = str(input('Nome: '))
nasc = int(input('Nascimento: '))
trabalhador['idade'] = datetime.now().year-nasc
trabalhador['ctps'] = int(input('Carteira de trabalho (0 caso não possua): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(input('Qual o ano da contratação: '))
    trabalhador['salário'] = float(input('Qual o salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] + 35) - datetime.now().year)
else:
    print('Sem registros na CTPS')
for k, v, in trabalhador.items():
    print(f'{k}: {v}')
