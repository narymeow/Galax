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
bg_img = pygame.image.load('Sources_img/backgroud.jpg')
bg = bg_img.get_rect(center=(DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2))

# Действия игры
while GAME_STATUS:
    bg.blit()
    DISPLAY.fill((255, 255, 255))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (user_x, user_y, 50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_STATUS = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            user_x -= speed
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 0:
            user_x += speed
        elif event.type == pygame.K_UP:
            user_y -= speed
        elif event.type == pygame.K_DOWN:
            user_y += speed
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
