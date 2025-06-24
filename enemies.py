import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, move_range=100, speed=2):
        super().__init__()
        self.img = pygame.image.load("assets/images/enemy/ghost.png")
        self.image = self.img
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.health = 2 

        self.start_x = x
        self.move_range = move_range  
        self.speed = speed
        self.direction = 1 

    def update(self):
        self.rect.x += self.speed * self.direction

        if abs(self.rect.x - self.start_x) >= self.move_range:
            self.direction *= -1

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.kill()
    
