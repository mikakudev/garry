import pygame
from settings import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill((100, 100, 100))  # Серый цвет
        self.rect = self.image.get_rect(topleft=(x, y))