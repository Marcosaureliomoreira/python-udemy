#Ex 036
'''Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor das prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.'''

casa = float(input('Digite o valor da casa R$:'))
salario = float(input('Digite o salário do comprador R$:'))
anos = int(input('Uqantos anos de financiamento : '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emorestimo pode ser CONCEDIDO!')
else:
    print('Empréstimo negado!')




