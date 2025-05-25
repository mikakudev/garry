# menu.py

import pygame
import sys
from settings import *


def draw_text(surface, text, x, y, font, color=BLACK):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)

def show_menu(screen, clock):
    font = pygame.font.Font(None, 60)  # Шрифт создаётся внутри функции — безопасно
    while True:
        screen.fill(SKY_BLUE)

        # Рисуем текст заголовка и подсказок
        draw_text(screen, "Boshy Clone", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3, font)
        draw_text(screen, "Press [SPACE] to Start", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font)
        draw_text(screen, "Press [ESC] to Quit", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, font)

        pygame.display.flip()  # Обновляем экран
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()