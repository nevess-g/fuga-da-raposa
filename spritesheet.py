# Importa o módulo os, usado para manipular caminhos de arquivos
import os

# Importa a biblioteca pygame
import pygame

# Importa constantes definidas no arquivo valores.py
from valores import *


# Cria a classe Raposa, que representa o personagem do jogador
# A classe herda de pygame.sprite.Sprite para aproveitar
# funcionalidades prontas do sistema de sprites do pygame
class Raposa(pygame.sprite.Sprite):

    # Método construtor da classe
    def __init__(self):

        # Inicializa a classe de Sprite
        pygame.sprite.Sprite.__init__(self)

        # Define o diretório onde estão as imagens da raposa
        # assets/img/Sprites
        sprite_dir = os.path.join("assets", "img", "Sprites")

        # ====== SPRITES DE MOVIMENTO ======

        def carrega_redimensiona(filename):
            image = pygame.image.load(os.path.join(sprite_dir, filename)).convert_alpha()
            scale = 0.6
            return pygame.transform.scale(
                image,
                (int(image.get_width() * scale), int(image.get_height() * scale)),
            )

        # Lista de imagens da animação andando para a esquerda
        self.sprites_left = [
            carrega_redimensiona("Esq1.png"),
            carrega_redimensiona("Esq2.png"),
            carrega_redimensiona("Esq3.png"),
        ]

        # Lista de imagens da animação andando para a direita
        self.sprites_right = [
            carrega_redimensiona("Dir1.png"),
            carrega_redimensiona("Dir2.png"),
            carrega_redimensiona("Dir3.png"),
        ]

        # Lista de imagens da animação andando para cima
        self.sprites_up = [
            carrega_redimensiona("Cima1.png"),
            carrega_redimensiona("Cima2.png"),
            carrega_redimensiona("Cima3.png"),
            carrega_redimensiona("Cima4.png"),
        ]

        # Lista de imagens da animação andando para baixo
        self.sprites_down = [
            carrega_redimensiona("Baixo1.png"),
            carrega_redimensiona("Baixo2.png"),
            carrega_redimensiona("Baixo3.png"),
        ]

        # Imagem usada quando a raposa está parada
        self.stopped_image = carrega_redimensiona("Parada.png")

        # =========================
        # CONTROLE DE ANIMAÇÃO
        # =========================

        # Direção inicial da raposa
        self.direction = "right"

        # Define a lista de sprites inicial
        self.sprites = self.sprites_right

        # Índice do frame atual da animação
        self.frame_index = 0

        # Temporizador usado para controlar velocidade da animação
        self.frame_timer = 0

        # Quantos ciclos esperar antes de trocar o frame
        self.frame_delay = 6

        # =========================
        # CONFIGURAÇÃO VISUAL
        # =========================

        # Define a imagem inicial da raposa
        self.image = self.stopped_image

        # Cria o retângulo da sprite
        # O rect é usado para posição e colisão
        self.rect = self.image.get_rect()

        # Define a posição inicial da raposa na tela
        self.rect.topleft = 100, 100

        # =========================
        # MOVIMENTO
        # =========================

        # Velocidade horizontal
        self.velocity_x = 0

        # Velocidade vertical
        self.velocity_y = 0

        # Velocidade padrão de movimentação
        self.speed = 5


    # Método update()
    # É chamado automaticamente no loop principal do jogo
    # Serve para atualizar posição e animações da raposa
    def update(self):

        # Move a raposa no eixo X
        self.rect.x += self.velocity_x

        # Move a raposa no eixo Y
        self.rect.y += self.velocity_y

        # =========================
        # LIMITES DA TELA
        # =========================

        # Impede que a raposa saia do mundo do mapa
        if self.rect.right > WORLD_WIDTH:
            self.rect.right = WORLD_WIDTH

        # Impede que saia pela esquerda
        if self.rect.left < 0:
            self.rect.left = 0

        # Impede que saia por cima
        if self.rect.top < 0:
            self.rect.top = 0

        # Impede que saia por baixo
        if self.rect.bottom > WORLD_HEIGHT:
            self.rect.bottom = WORLD_HEIGHT

        # =========================
        # DETECÇÃO DE DIREÇÃO
        # =========================

        # Se estiver andando para a esquerda
        if self.velocity_x < 0:
            self.direction = "left"
            self.sprites = self.sprites_left

        # Se estiver andando para a direita
        elif self.velocity_x > 0:
            self.direction = "right"
            self.sprites = self.sprites_right

        # Se estiver andando para cima
        elif self.velocity_y < 0:
            self.direction = "up"
            self.sprites = self.sprites_up

        # Se estiver andando para baixo
        elif self.velocity_y > 0:
            self.direction = "down"
            self.sprites = self.sprites_down

        # =========================
        # CONTROLE DE ANIMAÇÃO
        # =========================

        # Se a raposa estiver parada
        if self.velocity_x == 0 and self.velocity_y == 0:

            # Mostra imagem parada
            self.image = self.stopped_image

            # Reinicia animação
            self.frame_index = 0
            self.frame_timer = 0

        else:
            # Incrementa o temporizador da animação
            self.frame_timer += 1

            # Quando atingir o delay...
            if self.frame_timer >= self.frame_delay:

                # Reinicia o timer
                self.frame_timer = 0

                # Avança para o próximo frame
                # O operador % faz voltar ao início da lista
                self.frame_index = (
                    self.frame_index + 1
                ) % len(self.sprites)

            # Atualiza a imagem atual da sprite
            self.image = self.sprites[self.frame_index]