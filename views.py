from .models import *
from .main import *

import random

'''
def dificalty_actions(ct: content_type):
    if dificalty == 'normal':
        if ct == User:
            return {'hp': 50, 'speed': 5, 'damage': 10}
        elif ct == Mob:
            return {'hp': 5, 'speed': 3, 'damage': 10}
        elif ct == MobShot:
            return {'speed': 10}
    elif dificalty == 'hard':
        if ct == User:
            return {'hp': 30, 'speed': 3, 'damage': 7}
        elif ct == Mob:
            return {'hp': 5, 'speed': 4, 'damage': 13}
        elif ct == MobSpawner:
            return {'period': 3}
        elif ct == MobShot:
            return {'speed': 17}
    elif dificalty == 'easy':
        if ct == User:
            return {'hp': 60, 'speed': 7, 'damage': 13}
        elif ct == Mob:
            return {'hp': 3, 'speed': 2, 'damage': 7}
        elif ct == MobSpawner:
            return {'period': 8}
        elif ct == MobShot:
            return {'speed': 7}
'''

class Generate:

    @staticmethod
    def generic_mob():
        ''' Рандомно генерирует моба для передачи в MobSpawner '''
        if random.randint(1, dificalty_actions(MobSpawner)['period']) == 1:
            range_x = User.user_x - 100 - User.user_wight, User.user_x + 100 + User.user_wight
            range_y = User.user_y - 100 - User.user_height, User.user_y + 100 + User.user_height
            # Исключаем координаты в которых нельзя заспавнить моба
            no_spawn_cords = [
                (User.user_x + 20 + User.user_wight, User.user_x - 20 - User.user_wight),
                (User.user_y + 20 + User.user_height, User.user_y - 20 - User.user_height)
            ]
            random_x = User.user_x
            random_y = User.user_y

            # Цикл закончился, когда координаты моба будут валидны и функция вернёт координаты
            while random_x in range(*no_spawn_cords[0]) or random_y in range(*no_spawn_cords[1]):
                random_x = random.randint(*range_x)
                random_y = random.randint(*range_y)

            return {'mob_x': random_x, 'mob_y': random_y}

    @staticmethod
    def generate_menu():
        menu_w, menu_h = 500, 300
        menu_image = pygame.image.load('images/menu.').get_rect(center=DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2)
        menu = menu_image.get_rect(center=DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2)
        sound_icon_image = pygame.image.load('images/sound.')
        sound_icon = sound_icon_image.get_rect(buttom=menu.left[0] + menu_w // 4, menu.center[1] + menu_h // 2 - 20)
        difs_image = pygame.image.load('images/difs.')
        difs = difs_image.get_rect(center=DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2, difs_image.center[1] - 70)

        SpriteParams(difs_image, difs)
        SpriteParams(sound_icon_image, sound_icon)
        SpriteParams(menu_image, menu)

    @staticmethod
    def generate_pause_menu():
        pause_menu_w, pause_menu_h = 500, 300
        pause_menu_image = pygame.image.load('images/pause_menu.')
        pause_menu = pause_menu_image.get_rect(center=(DISPLAY_SIZE[0] // 2, DISPLAY_SIZE[1] // 2))
        start_button_image = pygame.image.load('images/start.')
        start_button = start_button_image.get_rect(center=DISPLAY_SIZE[0] // 2 - pause_menu_w // 2 - 50)
        leave_button_image = pygame.image.load('images/leave.')
        leave_button = leave_button_image.get_rect(center=DISPLAY_SIZE[0] // 2 + pause_menu_w // 2 + 50))

        SpriteParams(start_button_image, start_button)
        SpriteParams(leave_button_image, leave_button)
        SpriteParams(pause_menu_image, pause_menu)


def check_events():
    for event in pygame.events:
        if event.type == pygame.QIUT:
            GAME_STATUS = False
        elif event.type == pygame.K_LEFT:
            User(side='k_left', coord=User.user_x - User.speed)
        elif event.type == pygame.K_RIGHT:
            User(side='k_right', coord=User.user_x + User.speed)
        elif event.type == pygame.K_UP:
            User(side='k_up', coord=User.user_y - User.speed)
        elif event.type == pygame.K_BUTTOM:
            User(side='k_buttom', coord=User.user_y + User.spped)

def add_object(obj):
    if obj == Mob:
        mob.add(obj)
    elif obj == MobShot:
        mob_shots.add(obj)



