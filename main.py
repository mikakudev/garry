# main.py

import pygame
from settings import *
from menu import show_menu
from game import run_game


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Garry")
    clock = pygame.time.Clock()
    level_paths = [
        "levels/level1.txt",
        "levels/level2.txt",
        "levels/level3.txt",
        "levels/level4.txt",
        "levels/level5.txt",
        ]

    show_menu(screen, clock)
    run_game(screen, clock, level_paths)

if __name__ == "__main__":
    main()
