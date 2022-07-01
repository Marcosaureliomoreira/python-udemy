vel = float(input('Digite a velocidade:'))
if vel >80:

    print('Você foi multado! Você excedeu o límite de velocidade permitido que é de 80km/h')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R$:{:.2f}!'.format(multa))

print('Tenha um bom dia! Dirija com segurança!')
