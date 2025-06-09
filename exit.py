import pygame
from settings import TILE_SIZE

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img = pygame.image.load("assets/images/tiles/gate.png")
        self.image = self.img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)