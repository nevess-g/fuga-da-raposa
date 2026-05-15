import pygame
from valores import *
from spritesheet import *

# inicia o módulo do pygame
pygame.init()

# cria a janela do jogo
janela = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

game = True

while game:
    janela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    pygame.display.update()