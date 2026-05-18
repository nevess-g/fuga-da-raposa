import pygame
from valores import *
from spritesheet import *
from menu import *
import mapa

# inicia o módulo do pygame
pygame.init()

# cria a janela do jogo
janela = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# define o estado do jogo
estado_jogo = "menu"

# estrutura de dado para o andamento do loop
game = True

# agrupa todos os sprites
all_sprites = pygame.sprite.Group()

# instancia a classe Rapsoa
raposa = Raposa()

# instancia a classe Menu
menu = Menu()

# instancia a classe Fases
menu_fases = Fases()

while game:
    # define a velocidade do jogo
    clock.tick(FPS)

    # preenche a janela com preto
    janela.fill(PRETO)

    # itera sobre todos os eventos do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
        # verifica o estado do jogo
        if estado_jogo == "menu":
            # captura a posição do mouse
            pos_mouse = pygame.mouse.get_pos()
            resultado = menu.processar_eventos(event, pos_mouse)

            # define o novo estado do jogo de acordo com o botão pressionado
            if resultado == "jogar":
                estado_jogo = "fases"
            elif resultado == "sair":
                game = False
        
        elif estado_jogo == "fases":
            # captura a posição do mouse
            pos_mouse = pygame.mouse.get_pos()
            resultado = menu_fases.processar_eventos(event, pos_mouse) # feito com Copilot

            if resultado == "fase1":
                    estado_jogo = "jogando"
                    all_sprites.add(raposa)
                    mapa.iniciar_fase(1) # feito com Copilot
            elif resultado == "voltar":
                estado_jogo = "menu"
    
    if estado_jogo == "menu":
        # desenha o menu na surface da janela
        menu.desenhar(janela)
    elif estado_jogo == "fases":
        menu_fases.desenhar(janela)

    elif estado_jogo == "jogando":
        janela.fill(PRETO)
        # verifica as teclas pressionadas 
        keys = pygame.key.get_pressed()

        # zera as velocidades X e Y da raposa
        raposa.velocity_x = 0
        raposa.velocity_y = 0

        # altera a velocidade da raposa de acordo com a direção pressionada
        if keys[pygame.K_a]:
            raposa.velocity_x = -raposa.speed
        elif keys[pygame.K_d]:
            raposa.velocity_x = raposa.speed
        elif keys[pygame.K_w]:
            raposa.velocity_y = -raposa.speed
        elif keys[pygame.K_s]:
            raposa.velocity_y = raposa.speed

        # atualiza os sprites
        all_sprites.update()
        all_sprites.draw(janela)

        old_rect = raposa.rect.copy()
        all_sprites.update()
        mapa.atualizar(raposa, old_rect)
        mapa.desenhar(janela, all_sprites, raposa)
    
    # atualiza a tela
    pygame.display.update()