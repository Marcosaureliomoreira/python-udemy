#EX 043
'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:
-Abaixo de 18.5: Abaixo do peso
-Entre 18.5 e 25: Peso ideal
--25 até 30: Sobrepeso
-30 até 40: Obesidade
-Acima de 40: Obesidade mórbida'''

peso = float(input('Digite o peso: (kg) '))
altura = float(input('Digite a altura: (m) '))

imc = peso / (altura **2)
print('Seu IMC é {}'.format(imc))
if imc <18.5:
    print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABÉNS, você esta na sua faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

