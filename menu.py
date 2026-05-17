import os
import pygame
from valores import *

class Botao:
    # método construtor da classe Botão
    def __init__(self, x, y, largura, altura, texto, fonte):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.fonte = fonte
        self.ativo = False
    
    # métdodo utilizado para desenhar os botões na tela
    def desenhar(self, surface):

        # cria a sombra do botão se estiver ativo
        cor_sombra = PRETO
        if not self.ativo:
            offset_sombra = 4
        else:
            offset_sombra = 2
        
        # cria o retângulo da sombra
        sombra_rect = pygame.Rect(
            self.rect.x + offset_sombra,
            self.rect.y + offset_sombra,
            self.rect.width,
            self.rect.height
        )

        # desenha um retângulo na tela de acordo com os parâmetros anteriores
        pygame.draw.rect(surface, cor_sombra, sombra_rect, border_radius=8)

        # altera as cores do fundo e da borda se o botão estiver selecionado ou não
        if self.ativo:
            cor_fundo = (220, 140, 50)
            cor_borda_interna = (255, 180, 90)
        else:
            cor_fundo = (180, 100, 40)
            cor_borda_interna = (200, 120, 50)
        
        # desenha o btão na tela
        pygame.draw.rect(surface, cor_fundo, self.rect, border_radius=8)

        # desenha a borda mais escura do botão
        cor_borda_escura = (100, 60, 20)
        pygame.draw.rect(surface, cor_borda_escura, self.rect, 3, border_radius=8)
        
        # cria um retângulo de destque para quando o mouse passar por cima
        rect_destaque = pygame.Rect(
            self.rect.x + 3,
            self.rect.y + 3,
            self.rect.width - 6,
            self.rect.height - 6
        )
        pygame.draw.rect(surface, cor_borda_interna, rect_destaque, 1, border_radius=6)

        # altera a cor do texto se o botão estiver ativo
        if self.ativo:
            cor_texto = (255, 255, 200)
        else:
            cor_texto = BRANCO

        # renderiza o texto
        texto_renderizado = self.fonte.render(self.texto, False, cor_texto)
        
        # se o botão estiver ativo, o texto desce para dar a sensação de que foi pressionado
        if self.ativo:
            offset_y = -2
        else:
            offset_y = 0

        # define o retângulo que contém o texto
        texto_rect = texto_renderizado.get_rect(
            center=(self.rect.centerx, self.rect.centery + offset_y)
        )

        # desenha o texto no retângulo definido
        surface.blit(texto_renderizado, texto_rect)

    # verifica se o botão foi clicado
    def verificar_clique(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)

    # verifica se o mouse está em cima do botão
    def atualizar_hover(self, pos_mouse):
        self.ativo = self.rect.collidepoint(pos_mouse)

# cria a classe do menu principal do jogo
class Menu:

    # construtor da classe Menu
    def __init__(self):
        img_dir = os.path.join("assets", "img")
        font_dir = os.path.join("assets", "fonts")
        
        # carrega a logo e redimensiona
        logo_original = pygame.image.load(os.path.join(img_dir, "logo.png"))
        self.logo = pygame.transform.scale(logo_original, (540, 360))
        
        # carrega o fundo
        self.fundo = pygame.image.load(os.path.join(img_dir, "fundo.png"))
        
        # carrega fontes
        self.fonte_botoes = pygame.font.Font(
            os.path.join(font_dir, "PixelGameFont.ttf"), 40
        )

        # cria botões passando os parâmetros utilizados pelo constructor da classe Botão
        posicao_x_botoes = WIDTH // 2 - 100

        self.botao_jogar = Botao(
            posicao_x_botoes, HEIGHT // 2 + 50, 200, 60, "Jogar", self.fonte_botoes
        )
        self.botao_sair = Botao(
            posicao_x_botoes, HEIGHT // 2 + 150, 200, 60, "Sair", self.fonte_botoes
        )
        
        self.botoes = [self.botao_jogar, self.botao_sair]

    # método que desenha o fundo, logo e botões na tela
    def desenhar(self, surface):
        surface.blit(self.fundo, (0, 0))
        
        logo_rect = self.logo.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        surface.blit(self.logo, logo_rect)
        
        for botao in self.botoes:
            botao.desenhar(surface)
    
    # processa os eventos e atualiza o estado do jogo de acordo com o botão pressionado e atualiza o hover
    def processar_eventos(self, evento, pos_mouse):
        for botao in self.botoes:
            botao.atualizar_hover(pos_mouse)
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_jogar.verificar_clique(pos_mouse):
                return "jogar"
            elif self.botao_sair.verificar_clique(pos_mouse):
                return "sair"
        
        return None
    