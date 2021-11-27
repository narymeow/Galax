import pygame

from .init_objects import *

pygame.init()
dificalty = 'normal'
GAME_STATUS = True
DISPLAY_SIZE = 800, 600
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('star space game') # название игры в консоли
pygame.display.set_icon() # Иконка игры в консоли


def chek_status_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


# Действия игры
while GAME_STATUS:
    chek_status_game()
    pygame.draw.rect(DISPLAY, )

    pygame.time.Clock().tick(60) # Ограничеваем частоту кадров до 60 FPS
