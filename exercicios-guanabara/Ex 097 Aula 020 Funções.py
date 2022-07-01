# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho
# adaptável.
# Ex:
# escreva('Olá Mundo')
# Saída:
# ~~~~~~~~~
#Olá mundo
# ~~~~~~~~~


'''def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)



escreva('Gustavo Guanabara')
escreva('Curso de Python no youtube')
escreva('Estou Adorando')'''



'''def escreva(frase):
    tam = len(frase) + 4
    print('-' * tam)
    print(f'  {frase}')
    print('-' * tam)


escreva('Marcos Aurélio Moreira das Dores')
escreva('Oi')'''

def escreva(msg):
    """
    > Imprimi uma mensagem na tela com as as linhas pontilhadas adaptável ao tamanho da mensagem.
    :param msg: Mensagem a ser exibida.
    :return: Retorna a mensagem.
    """

    tam = len(msg)
    print('-' * tam)
    print(msg)
    print('-' * tam)






escreva('Marcos Aurélio')
help(escreva)








