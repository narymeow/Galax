import pygame


pygame.init()
dificalty = 'normal'

GAME_STATUS = True
DISPLAY_SIZE = 1400, 1000
mobs = pygame.sprite.Group()
mob_shots = pygame.sprite.Group()
DISPLAY = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('Квадрат малевича') # название игры в консоли
speed = 30
user_x, user_y = DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2
bg = pygame.image.load('Sources_img/background.jpg')
dron = pygame.image.load('Sources_img/dron1.png')

# Действия игры
while GAME_STATUS:
    DISPLAY.fill((255, 255, 255))
    DISPLAY.blit(bg, (100, 100))
    DISPLAY.blit(dron, (user_x, user_y, 20, 20))
    keys = pygame.mouse.get_pressed()
    if keys[pygame.K_LEFT]:
        user_x -= speed
    elif keys[pygame.K_RIGHT]:
        user_x += speed
    if user_x > DISPLAY_SIZE[0]:
        user_x = DISPLAY_SIZE[0] // 2
    elif user_x < 0:
        user_x = DISPLAY_SIZE[0] // 2
    elif user_y > DISPLAY_SIZE[1]:
        user_y = DISPLAY_SIZE[1] // 2
    elif user_y < 0:
        user_y = DISPLAY_SIZE[1] // 2

    pygame.display.update()
    pygame.time.Clock().tick(60) # Ограничеваем частоту кадров до 60 FPS
