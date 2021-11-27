from .models import *
from .main import dificalty

import random


def dificalty_actions(ct: content_type):
    ''' Обработчик сложности.
    Если в инициализации объекта нам нужно работать со сложностью мы вызываем её '''
    if dificalty == 'normal':
        if ct == User:
            return {'hp': 50, 'speed': 5, 'damage': 10}
        elif ct == Mob:
            return {'hp': 5, 'speed': 3, 'damage': 10}
        elif ct == MobSpawner:
            return {'period': 5}
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


def generic_mob():
    ''' Рандомно генерирует моба для передачи в MobSpawner '''
    if random.randint(1, dificalty_actions(MobSpawner)) == 1:
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

