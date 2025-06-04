import pygame
from settings import *

class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.spikeimg = pygame.image.load("assets/images/tiles/spike.png").convert_alpha()
        self.image = self.spikeimg
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)