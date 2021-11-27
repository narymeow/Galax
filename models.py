from .main import DISPLAY_SIZE
from .views import *


class User:
    '''С помощью new мы имеем только один экземпляр класса'''
    __instance = None
    user_x = DISPLAY_SIZE[0] * 0.5
    user_y = DISPLAY_SIZE[1] * 0.5
    user_side = 'left'

    user_wight = 80
    user_height = 70
    mob_list = []
    mob_shot_list = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(User, cls).__new__(cls)
        return cls.__instance

    def __init__(self, user_x, user_y, side, **kwargs):
        ''' Инициализируем обязательнык данные '''
        self.user_x = user_x
        self.user_y = user_y
        self.side = side
        if kwargs:
            if 'get_damage' in kwargs.values():
                func = kwargs['func']
                self.hp = func['hp']
            elif 'change_difficult' in kwargs.values():
                self.speed = func['speed']
                self.damage = func['damage']

    @staticmethod
    def event():
        ''' Вызываем это функцию, когда происходят особеные события с пользователем '''
        return User(func=dificalty_actions(User))


class MobSpawner:

    def __init__(self):
        mob = generic_mob()
        if mob:
            self.mob_x = mob['mob_x']
            self.mob_y = mob['mob_y']


class Mob(MobSpawner):
    ''' ширина и высота это постоянные переменные '''
    mob_wight = 50
    mob_height = 60

    def event(self, event):
        if event == 'mob_dead':
            del mob_list[self]
        elif event == 'mob_shot':
            User.mob_shot_list.append(MobShot(self.mob_x, self.mob_y))


class MobShot:
    ''' Для этого класса нужно написать логику во views '''
    mob_shot_wight = 8
    mob_shot_height = 2

    def __init__(self, shot_x, shot_y, side, **kwargs):
        self.shot_x = shot_x
        self.shot_y = shot_y
        self.side = side
        if kwargs:
            self.speed = kwargs['func']['speed']

    @staticmethod
    def event():
        return MobShot(func=dificalty_actions(MobShot))



















