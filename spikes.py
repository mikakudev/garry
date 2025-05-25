import pygame
from settings import *

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE), pygame.SRCALPHA)
        pygame.draw.polygon(
            self.image,
            (200, 0, 200),
            [(0, TILE_SIZE), (TILE_SIZE // 2, 0), (TILE_SIZE, TILE_SIZE)]
        )
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)