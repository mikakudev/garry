import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img = pygame.image.load("assets/images/enemy/ghost.png")
        self.image = self.img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 2 

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()