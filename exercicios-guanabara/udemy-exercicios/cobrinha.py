#método init da cobrinha
class Cobra:
    def __init__(self, tam_tela=(300, 400),
                        posicao=[80, 50],# [esquerda, cima]
                        corpo=[[80, 50], [70, 50], [60, 50]],
                        direcao ='DIREITA'):

        self.tam_tela = tam_tela
        self.posicao = posicao
        self.corpo = corpo
        self.direcao = direcao

