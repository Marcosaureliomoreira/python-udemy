# A primeira coisa a se fazer para criar uma interface gráfica é criar a janela.
# Label: é um texto de orienação para o usuário, orientando o que é pra fazer.
# text: Para passar o texto a ser lido dentro da janela.
# grid: método usado para escolher a posição do texto dentro da janela.
# column: coluna dentro da janela.
# row: linha dentro da janela.
# Button(): Para criar um botão para o usuário clicar dentro da janela.
# command: significa comando. ao clicar no botão será executado o comando.
# padx: espaço entre o texto, espaço de um lado para o outro.
# pady: espaço de cima para baixo.

#obs: para executar o código na janela temos que coloca-lo dentro de uma "Função", sem "parâmetros" e retornos, como abaixo:
#obs: ao final quando dar-mos o comando temos que colocar a função sem o parêntese, ao lado de command.

import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes['text'] = texto # Editando o parâmetro texto(text) do texto_cotações.

    #print(texto)# essa linha á apagada.
#pegar_cotacoes() # essa linha é apagada após


janela = Tk()  # Comando para criar uma janéla para o código.
janela.title('Cotação Atual das Moedas') # Para alterar o nome a da janela.
#janela.geometry('400x400') # fixa o tamanho da janela em 400.

texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas')
texto_orientacao.grid(column=0, row=0, padx=10, pady=10) # Adicionando o texto por colunas e linhas, para saber a posição do texto.

botao = Button(janela, text='Buscar cotações Dolar/Euro/BTC', command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10) # Adicionado uma posição para o botão.

texto_cotacoes = Label(janela, text='') # dentro de "text" pode ser um texto vazio, pode passar alguma informação.
texto_cotacoes.grid(column=0, row=2, padx=10, pady=10) # posição do botão clicável, para exibir cotação das moedas.



janela.mainloop() # Permite que a janela continue na tela e só feche quando quisermos.