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