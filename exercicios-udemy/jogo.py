import pygame
import sys
from cobrinha import Cobra

# inicializando o pygame
pygame.init()
TAM_TELA = (300, 400)
tela = pygame.display.set_mode(TAM_TELA)
cobra = Cobra()

# Iniciando o loop do jogo
while True:
    tela.fill((7, 0, 35)) # RGB - Red, Green, Blue - (255, 255, 255)
    for event in pygame.event.get():
        # listener - mouse ou teclado
        if event.type == pygame.QUIT:
            # interrompe pygame
            pygame.quit()
            # fechar script (janela)
            sys.exit()

    # Desenha a cobra
    for pos in cobra.corpo:
        pygame.draw.rect(tela,  pygame.Color(255, 204, 0),
                                # esquerda, cima, largura, altura
                                pygame.Rect(pos[0], pos[1], 10, 10))

    # Atualiza a tela a cada frame
    pygame.display.update()







