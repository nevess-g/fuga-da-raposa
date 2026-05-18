import pygame
from valores import *

# este código foi feito pelo Copilot

MAP_FILES = {
    1: MAP_IMAGE,
    2: MAP_IMAGE,
    3: MAP_IMAGE,
}

FASE_STARTS = {
    1: (WORLD_WIDTH // 2 + 20, WORLD_HEIGHT // 2 + 10),
    2: (WORLD_WIDTH // 2 + 20, WORLD_HEIGHT // 2 + 10),
    3: (WORLD_WIDTH // 2 + 20, WORLD_HEIGHT // 2 + 10),
}

fase_atual = None
map_surface = None
allowed_rect = pygame.Rect(FENCE_MARGIN, FENCE_MARGIN, WORLD_WIDTH - 2 * FENCE_MARGIN, WORLD_HEIGHT - 2 * FENCE_MARGIN)


def iniciar_fase(fase):
    global fase_atual, map_surface, allowed_rect
    if fase not in MAP_FILES:
        fase = 1
    fase_atual = fase
    imagem_fase = pygame.image.load(MAP_FILES[fase]).convert_alpha()
    map_surface = pygame.transform.scale(imagem_fase, (WORLD_WIDTH, WORLD_HEIGHT))
    allowed_rect = pygame.Rect(FENCE_MARGIN, FENCE_MARGIN, WORLD_WIDTH - 2 * FENCE_MARGIN, WORLD_HEIGHT - 2 * FENCE_MARGIN)


def get_start_pos(fase):
    return FASE_STARTS.get(fase, FASE_STARTS[1])


def atualizar(raposa, old_rect):
    if map_surface is None:
        return
    if not allowed_rect.contains(raposa.rect):
        raposa.rect = old_rect


def desenhar(surface, grupo, raposa):
    if map_surface is None:
        surface.fill(PRETO)
        return

    camera_x = raposa.rect.centerx - WIDTH // 2
    camera_y = raposa.rect.centery - HEIGHT // 2
    camera_x = max(0, min(camera_x, WORLD_WIDTH - WIDTH))
    camera_y = max(0, min(camera_y, WORLD_HEIGHT - HEIGHT))

    surface.blit(map_surface, (-camera_x, -camera_y))
    for sprite in grupo:
        surface.blit(sprite.image, sprite.rect.move(-camera_x, -camera_y))
