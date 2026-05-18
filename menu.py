import os
import pygame
from valores import *

class Botao:
    # método construtor da classe Botão
    def __init__(self, x, y, largura, altura, texto, fonte, habilitado=True):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.fonte = fonte
        self.ativo = False
        self.habilitado = habilitado
    
    # métdodo utilizado para desenhar os botões na tela
    def desenhar(self, surface):

        # cria a sombra do botão se estiver ativo
        cor_sombra = PRETO
        if self.ativo and self.habilitado:
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
        if self.habilitado:
            if self.ativo:
                cor_fundo = LARANJA_ATIVO
            else:
                cor_fundo = MARROM_DESABILITADO
            cor_borda_interna = LARANJA_BORDA_CLARA
        else:
            cor_fundo = INATIVO
            cor_borda_interna = BORDA_INATIVA
        
        # desenha o btão na tela
        pygame.draw.rect(surface, cor_fundo, self.rect, border_radius=8)

        # desenha a borda mais escura do botão
        cor_borda_escura = MARROM_ESCURO
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
            cor_texto = AMARELO_TEXTO_ATIVO
        else:
            cor_texto = TEXTO_INATIVO

        # renderiza o texto
        texto_renderizado = self.fonte.render(self.texto, False, cor_texto)
        
        # se o botão estiver ativo, o texto desce para dar a sensação de que foi pressionado
        if self.ativo and self.habilitado:
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
        return self.rect.collidepoint(pos_mouse) and self.habilitado

    # verifica se o mouse está em cima do botão
    def atualizar_hover(self, pos_mouse):
        self.ativo = self.rect.collidepoint(pos_mouse) and self.habilitado

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

class Fases:
    def __init__(self):
        img_dir = os.path.join("assets", "img")
        font_dir = os.path.join("assets", "fonts")

        self.fundo = pygame.image.load(os.path.join(img_dir, "fundo.png"))
        self.fonte_botoes = pygame.font.Font(os.path.join(font_dir, "PixelGameFont.ttf"), 40)
        self.fonte_titulo = pygame.font.Font(os.path.join(font_dir, "PixelGameFont.ttf"), 56)

        button_size = 150
        spacing = 50
        start_x = WIDTH // 2 - (3 * button_size + 2 * spacing) // 2
        y_fases = HEIGHT // 2 - button_size // 2

        self.botao_fase1 = Botao(start_x, y_fases, button_size, button_size, "Fase 1", self.fonte_botoes, habilitado=True) # feito com Copilot
        self.botao_fase2 = Botao(start_x + button_size + spacing, y_fases, button_size, button_size, "Fase 2", self.fonte_botoes, habilitado=False) # feito com Copilot
        self.botao_fase3 = Botao(start_x + 2 * (button_size + spacing), y_fases, button_size, button_size, "Fase 3", self.fonte_botoes, habilitado=False) # feito com Copilot
        self.botao_voltar = Botao(WIDTH // 2 - 80, y_fases + button_size + 60, 160, 60, "Voltar", self.fonte_botoes) # feito com Copilot

        self.botoes = [self.botao_fase1, self.botao_fase2, self.botao_fase3, self.botao_voltar] # feito com Copilot

    def desenhar(self, surface):
        surface.blit(self.fundo, (0, 0))

        titulo = self.fonte_titulo.render("Selecione a fase", False, BRANCO)
        titulo_rect = titulo.get_rect(center=(WIDTH // 2, HEIGHT // 5)) # feito com Copilot
        surface.blit(titulo, titulo_rect)

        for botao in self.botoes:
            botao.desenhar(surface)
    
    def processar_eventos(self, evento, pos_mouse):
        for botao in self.botoes:
            botao.atualizar_hover(pos_mouse)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_fase1.verificar_clique(pos_mouse):
                return "fase1"
            elif self.botao_voltar.verificar_clique(pos_mouse):
                return "voltar"

        return None