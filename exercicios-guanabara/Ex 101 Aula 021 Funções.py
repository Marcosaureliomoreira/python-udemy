# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando
# o valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL, OBRIGATÓRIO nas  eleições.
'''def voto(nascimento):
    from datetime import datetime, date
    idade = datetime.now().year - nascimento
    if idade == 16 or idade == 17 or idade >= 65:
        print(f'Você tem {idade} anos. VOTO OPCIONAL!')      # MINHA SOLUÇÃO. SEM O return.
    elif 18 <= idade < 65:
        print(f'Você tem {idade} anos. VOTO OBRIGATÓRIO!')
    else:
        print(f'Você tem {idade} anos. NÃO VOTA!')

    #print(f'Você nasceu no ano de {nascimento} e a sua idade é {idade}')

nasc = int(input('Digite o ano do seu nascimento: '))
voto(nasc)'''




'''def voto(nascimento):
    from datetime import datetime, date
    idade = datetime.now().year - nascimento
    if idade == 16 or idade == 17 or idade >= 65:
        return f'Você tem {idade} anos. VOTO OPCIONAL!'
    elif 18 <= idade < 65:
        return f'Você tem {idade} anos. VOTO OBRIGATÓRIO!'    #SOLUÇÃO COM O return.
    else:
        return f'Você tem {idade} anos. NÃO VOTA!'



nasci = int(input('Qual o seu ano de nascimento? '))
print(voto(nasci))'''



'''def voto(ano):
    from datetime import datetime, date
    idade = datetime.now().year - ano
    if 16 <= idade <= 17 or idade > 65:
        return f'Você tem {idade} anos, portanto: VOTO OPCIONAL!'
    elif 18 <= idade < 65:
        return f'Você tem {idade} anos, portanto: VOTO OBRIGATÓRIO!'
    else:
        return f'Você tem {idade} anos. portanto: NÃO VOTA!'


nascimento = int(input('Digite o ano do nascimento: '))
print(voto(nascimento))'''



def voto(nasc):
    from datetime import datetime
    idade = datetime.now().year - nasc
    if 16 <= idade <= 17 or idade > 65:
        print(f'Você tem {idade} anos. \033[34mVOTO OPCIONAL!\033[m')
    elif 18 <= idade < 65:
        print(f'Você tem {idade} anos. \033[31mVOTO OBRIGATÓRIO!\033[m')
    else:
        print(f'Você tem {idade} anos. \033[35mNÃO VOTA!\033[m')





# programa principal
nascimento = int(input('Ano de nascimeno: '))
voto(nascimento)







