

'''def mostraLinha():
    print('---------------------')

mostraLinha()
print('      SISTEMA DE ALUNOS       ')
mostraLinha()
mostraLinha()
print('     CADASTRO DE FUNCIONÁRIOS      ')
mostraLinha()
mostraLinha()
print('     ERRO DO SISTEMA      ')
mostraLinha()'''




'''def lin():     # Depos do comando "def" posso usar qualquer nome, qualquer tamanho para finalizar a linha. 
    print('-' * 30)

lin()
print('CURSO EM VÍDEO')
lin()
print('APRENDA PYTHON')
lin()
print('GUSTAVO GUANABARA')
lin()'''

'''def título(txt):     #FUNÇÕES COM PARÂMETRO
    print('-' * 30 )
    print(txt)
    print('-' * 30)

título('   CURSO EM VÍDEO    ')
título('   ESTOU APRENDENDO PYTHON    ')'''


                                            #PARTE PRÁTICA

'''def soma(a, b):
    soma = a, b
    print(soma)


#Programa Principal
soma(4, 4)
soma(8, 9)
soma(2, 1)'''

                                            # CRIANDO A FUNÇÃO "SOMA"
'''def soma(a, b):
    #print(f'A = {a} e B = {b}')
    soma = a + b
    print(f'A soma A + B = {soma}')


# Programa principal
soma(4, 5)
soma(7, 2)'''


                                            # CRIANDO DESEMPACOTADOR(TUPLAS)

# ABAIXO CRIEI UM CONTADOR E UMA FUNÇÃO PADRÃO QUE VAI MOSTRAR OS NÚMEROS NA TELA E CONTAR ELES.
'''def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} com {tamanho} números.')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

                                              # CRIANDO UMA FUNÇÃO PARA DOBRAR VALORES EM LISTAS.
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

'''def soma(*valores):
    soma = 0
    for num in valores:
        soma += num
    print(f'somando os valores {valores} temos {soma}')


soma(5, 2)
soma(2, 9, 4)'''

