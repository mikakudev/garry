import pygame
import sys
from settings import *
from player import Player
from tiles import Platform
from spikes import Spike
from exit import Exit
from enemies import Enemy


def load_level(path):
    level_data = []
    with open(path, "r") as f:
        for line in f:
            level_data.append(list(line.strip('\n')))
    return level_data


def build_level(level_data):
    platforms = pygame.sprite.Group()
    spikes = pygame.sprite.Group()
    exits = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    player_start = None

    for y, row in enumerate(level_data):
        for x, tile in enumerate(row):
            world_x = x * TILE_SIZE
            world_y = y * TILE_SIZE

            if tile == '#':
                platforms.add(Platform(world_x, world_y))
            elif tile == '^':
                spikes.add(Spike(world_x, world_y))
            elif tile == 'E':
                exits.add(Exit(world_x, world_y))
            elif tile == 'k':
                enemies.add(Enemy(world_x, world_y))
            elif tile == 'p':
                player_start = (world_x, world_y)

    return platforms, spikes, exits, enemies, player_start


def run_game(screen, clock, level_paths, current_level_index=0):
    if current_level_index >= len(level_paths):
        print("Все уровни пройдены!")
        pygame.quit()
        sys.exit()

    level_path = level_paths[current_level_index]

    level_data = load_level(level_path)
    platforms, spikes, exits, enemies, player_start = build_level(level_data)

    if player_start is None:
        raise ValueError("Нет точки спавна игрока (символ 'p') в карте уровня")

    player = Player(*player_start)
    all_sprites = pygame.sprite.Group(*platforms, *spikes, *exits, *enemies, player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        player.update(keys, platforms)
        player.bullets.update()
        player.bullets.draw(screen)

        # Проверка попаданий пуль по врагам
        for bullet in player.bullets:
            hit_enemies = pygame.sprite.spritecollide(bullet, enemies, False, pygame.sprite.collide_mask)
            for enemy in hit_enemies:
                enemy.take_damage()
                bullet.kill()

        # Проверка на столкновение с шипами
        for spike in spikes:
            if pygame.sprite.collide_mask(player, spike):
                return run_game(screen, clock, level_paths, current_level_index)

        # Проверка на достижение выхода
        if pygame.sprite.spritecollide(player, exits, False, pygame.sprite.collide_mask):
            return run_game(screen, clock, level_paths, current_level_index + 1)

        screen.fill(SKY_BLUE)
        all_sprites.draw(screen)
        player.bullets.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)