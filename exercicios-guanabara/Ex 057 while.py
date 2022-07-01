#Ex 057
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
#digitação novamente até ter um valor correto.



'''sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo registrado com sucesso'.format(sexo))'''


'''sexo = str(input('Digite o sexo: M/F')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Estes dados são inválidos. Por favor, Informe seu sexo:')).strip().upper()[0]
print('Sexo registrado com sucesso.'.format(sexo))'''














sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, digite o seu sexo: ')).upper().strip()
if sexo == 'F':
    print('Você é o do sexo feminino!')
    print('SEXO REGISTRADO COM SUCESSO.')
elif sexo == 'M':
    print('Você é do sexo masculino!')
    print('SEXO REGISTRADO CO SUCESSO!')


