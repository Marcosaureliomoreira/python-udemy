

def decodificando_listas_utf8(lista):
    for i in lista:
        print(i.decode('utf-8'))


def decodificando_listas_utf16(lista):
    for i in lista:
        print(i.decode('utf-16'))


def trabalhando_bytes(txt=''):
    todas_acentuadas = []
    acentuadas_utf8 = []
    texto = 'Fácil, Aurélio'
    # aqui codifica apenas as palavras acentuadas.
    if txt.upper() == 'codificar'.upper() or txt.upper() == 'codificar8'.upper():
        t = texto.encode('utf-8')
        acentuadas_utf8.append(t)
        print(acentuadas_utf8, '- Codificado')
        decodificando_listas_utf8(acentuadas_utf8) # função para decodificar apenas as palavras acentuadas utf-8.
    # aqui codifica todas as palavras.
    elif txt.upper() == 'codificar16'.upper():
        t = texto.encode('utf-16')
        todas_acentuadas.append(t)
        print(todas_acentuadas, '- Codificado')
        decodificando_listas_utf16(todas_acentuadas) # função para decodificar o texto com utf-16.
    else:
        t = texto
        print(t)


#trabalhando_bytes('codificar8')


def fatiamento_de_bytes(txt):
    """
    :param txt: Recebe o fatiamento do byte conforme a preferência do usuário.
    :return: Retorna o byte fatiado.
    """
    t = txt[1:3]
    tc = t.encode('utf-8')
    print(tc)





def representacao_numerica_bytes(numero):
    num = int(input(numero))
    print(f'O número {num} é representado pelo caractere {chr(num)}.')


#representacao_numerica_bytes('Digite um número para saber sua representação em caracter: ')



from random import choice

def sorteando_caracter():
    """
    :return: Retorna para o usuário o caracter que representa o número sorteado.
    """
    sorteio = []
    for c in range(0, 10000):
        sorteio.append(c)
    #print(sorteio)
    s = choice(sorteio)
    print(f'{s} = {chr(s)}')



def escrever_arquivos():
    with open('testando.txt', 'w', encoding='utf8') as file:
        file.write('Pelé')


escrever_arquivos()


def lendo_arquivo():
    """
    :return: O arquivo será lido de acordo com a preferência do usuário.
    """
    msg = 'Digite [1] para ler em utf-8 \nDigite [2] para ler em latin1'
    print(msg)
    print()
    ler = int(input('Como deseja ler o arquivo? '))
    if ler == 1:
        with open('testando.txt', 'r', encoding='utf8') as f:
            print(f.read())
    elif ler == 2:
        with open('testando.txt', 'r', encoding='latin1') as f:
            print(f.read())
    else:
        print('Opção inválida!')