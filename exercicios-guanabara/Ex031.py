distancia = float(input('Qual a distância da viagem?'))
print('Você esta prestes a começar uma viajem de {}km.'.format(distancia)) #CONDIÇÃO COMPOSTA.
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))

'''distancia = float(input('Qual é a distância de sua viagem?'))
print('Você esta prestes a começar uma viagem de {}km. '.format(distancia)) 
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))''' # FORMA SIMPLIFICADA DE SE FAZER.

