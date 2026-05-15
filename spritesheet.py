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

        # Lista de imagens da animação andando para a esquerda
        self.sprites_left = [
            pygame.image.load(os.path.join(sprite_dir, "Esq1.png")),
            pygame.image.load(os.path.join(sprite_dir, "Esq2.png")),
            pygame.image.load(os.path.join(sprite_dir, "Esq3.png")),
        ]

        # Lista de imagens da animação andando para a direita
        self.sprites_right = [
            pygame.image.load(os.path.join(sprite_dir, "Dir1.png")),
            pygame.image.load(os.path.join(sprite_dir, "Dir2.png")),
            pygame.image.load(os.path.join(sprite_dir, "Dir3.png")),
        ]

        # Lista de imagens da animação andando para cima
        self.sprites_up = [
            pygame.image.load(os.path.join(sprite_dir, "Cima1.png")),
            pygame.image.load(os.path.join(sprite_dir, "Cima2.png")),
            pygame.image.load(os.path.join(sprite_dir, "Cima3.png")),
            pygame.image.load(os.path.join(sprite_dir, "Cima4.png")),
        ]

        # Lista de imagens da animação andando para baixo
        self.sprites_down = [
            pygame.image.load(os.path.join(sprite_dir, "Baixo1.png")),
            pygame.image.load(os.path.join(sprite_dir, "Baixo2.png")),
            pygame.image.load(os.path.join(sprite_dir, "Baixo3.png")),
        ]

        # Imagem usada quando a raposa está parada
        self.stopped_image = pygame.image.load(
            os.path.join(sprite_dir, "Parada.png")
        )

        # ====== CONTROLE DE ANIMAÇÃO ======

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