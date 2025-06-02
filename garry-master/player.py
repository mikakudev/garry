import pygame
from settings import *
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Размер визуального спрайта и хитбокса
        width = TILE_SIZE - 8  # 24
        height = TILE_SIZE - 4  # 28
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (22, 127, 73), self.image.get_rect())
        self.rect = self.image.get_rect(topleft=(x + 4 , y + 4))

        self.mask = pygame.mask.from_surface(self.image)
        self.jump_pressed = False  # предотвращает множественные прыжки при удержании

        self.vel_y = 0
        self.on_ground = False
        self.jump_count = 0

        self.start_x = x
        self.start_y = y

        self.bullets = pygame.sprite.Group()
        self.shoot_cooldown = 0
        self.facing = 1
        self.health = 1

    def update(self, keys, platforms):
        dx = 0
        dy = 0

        # Движение
        if keys[pygame.K_LEFT]:
            dx = -5
            self.facing = -1
        if keys[pygame.K_RIGHT]:
            dx = 5
            self.facing = 1

        # Прыжок — только при нажатии (не удержании)
        if keys[pygame.K_SPACE]:
            if not self.jump_pressed and self.jump_count < 2:
                self.vel_y = -15
                self.jump_count += 1
                self.jump_pressed = True
        else:
            self.jump_pressed = False  # сброс когда клавиша отпущена

        # Гравитация
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Горизонтальное движение и столкновения
        self.rect.x += dx
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dx > 0:
                    self.rect.right = platform.rect.left
                if dx < 0:
                    self.rect.left = platform.rect.right

        # Ограничение по краям экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # Вертикальное движение и столкновения
        self.rect.y += dy
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if dy > 0:
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                    self.jump_count = 0  # сброс прыжков
                elif dy < 0:
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

        # Обработка стрельбы
        if keys[pygame.K_z] and self.shoot_cooldown == 0:
            self.shoot()
            self.shoot_cooldown = 15  # задержка между выстрелами

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.topleft = (self.start_x, self.start_y)
            self.vel_y = 0
            self.jump_count = 0

        self.bullets.update()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.facing)
        self.bullets.add(bullet)
