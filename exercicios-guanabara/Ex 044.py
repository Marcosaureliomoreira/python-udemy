#EX 044
'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
-á vista dinheiro/cheque:10% de desconto
-á vista no cartão:5% de desconto
-em até 2x no cartão:preço normal
-3x ou mais no cartão:20% de juros'''

print('{:=^40}'.format('LOJAS MOREIRA'))
preço =float (input('preço das compras: R$'))
print('''FORMAS DE PAGAMENTO:
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão''')
opção = int(input ('Qual a opção?'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(parcela))
elif opção== 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f}:.2f COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDADA de pagamento. Tente novamente!')
print('Sua compra de R$ {:.2f} vai custarn R$ {:.2f} no final'.format(preço, total))