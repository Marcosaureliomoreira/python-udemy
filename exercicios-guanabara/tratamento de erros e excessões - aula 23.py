'''a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / 'b'# TypeError / Erro de Tipo: um tipo de erro entre as variáveis. nesse caso uma inteira e um str.
print(f'O resultado é {r}')'''
#=======================================================================================================================

'''print(x) 
# NameError: A variável x não foi definida.'''
#=======================================================================================================================

'''lst = [3, 6, 4]
print(lst[3])'''
# O exemplo acima mostrará 'IndexError' pois nas lista os indices iniciam-se a partir do zero.
#=======================================================================================================================

#import uteis
#Caso o módulo de importação não seja encontrado será mostrado Um aviso de erro: 'ModuloNotFoundError'

#"exception" significa "exceção"
#=======================================================================================================================
'''try:  #Tenta fazer algo...
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b                                                           #Maneira1 de usar exception
except:  #Se não conseguir...                                           #Isso de chama Tratamento de erro.
    print(f'Infelizmente tivemos um problema :(')
else:  #O que vai acontecer se der certo
    print(f'O resultado é {r:.1f}')
finally:  #vai acontecer independente se der certo ou errado.
    print('Volte Sempre! Muito obrigado!')'''
#=======================================================================================================================





'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b                                                        #Maneira2
except:                                            #Isso de chama Tratamento de erro.
    print(f'Infelizmente tivemos um problema :(')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito obrigado!')'''










try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b                                                        #Maneira3 dentre várias
except (ValueError, TypeError):                                            #Isso de chama Tratamento de erro.
    print('Tivemos um probleama com os tipos de dados que você inseriu. :(')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário decidiu não informar os seu dados')
except Exception as erro:
    print(f'O erro foi encontrado {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte Sempre! Muito obrigado!')

















