import pygame
from settings import *

class Platform(pygame.sprite.Sprite):

    tile = pygame.image.load("assets/images/tiles/block.png")

    def __init__(self, x, y):
        super().__init__()
        self.image = Platform.tile
        self.rect = self.image.get_rect(topleft=(x, y))