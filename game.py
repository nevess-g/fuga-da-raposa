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

all_sprites = pygame.sprite.Group()
raposa = Raposa()
all_sprites.add(raposa)

while game:
    clock.tick(FPS)
    janela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()
    raposa.velocity_x = 0
    raposa.velocity_y = 0
    if keys[pygame.K_a]:
        raposa.velocity_x = -raposa.speed
    elif keys[pygame.K_d]:
        raposa.velocity_x = raposa.speed
    elif keys[pygame.K_w]:
        raposa.velocity_y = -raposa.speed
    elif keys[pygame.K_s]:
        raposa.velocity_y = raposa.speed

    all_sprites.update()
    all_sprites.draw(janela)
    pygame.display.update()