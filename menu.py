# menu.py

import pygame
import sys
from settings import *
from button import Button


def draw_text(surface, text, x, y, font, color=BLACK):
    render = font.render(text, True, color)
    rect = render.get_rect(center=(x, y))
    surface.blit(render, rect)

def show_menu(screen, clock):
    font = pygame.font.Font(None, 60)  # Шрифт создаётся внутри функции — безопасно
    bg_menu = pygame.image.load("assets/images/bg_menu.png")

    def start_game():
        return "start"

    def quit_game():
        pygame.quit()
        sys.exit()

    buttons = [
        Button(100, 350, 400, 60, "Начать игру", font, (0, 200, 0), WHITE, start_game),
        Button(100, 450, 400, 60, "Выйти", font, (0, 200, 0), WHITE, quit_game),
    ]

    while True:
        screen.blit(bg_menu, (0,0))

        # Рисуем текст заголовка и подсказок
        draw_text(screen, "Гарри Потный", 700, 200, font, WHITE)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()  # Обновляем экран
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.key == pygame.K_ESCAPE:
                    quit_game()
            #обработка кнопок
            for button in buttons:
                result = button.handle_event(event)
                if result == "start":
                    return