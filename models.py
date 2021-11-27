from .main import DISPLAY_SIZE
from .views import *
from pygame.sprite import Sprite
import pygame


class SpriteParams(Sprite):
    ''' Шаблон для создания спрайтов или одиночных поверхностей '''

    def __init__(self, rect, **kwargs):
        Sprite.__init__(self)
        self.image = pygame.draw.rect((50, 50), (255, 100, 0))
        self.rect = self.image
        if kwargs['side'] == 'k_left':
            self.x = kwargs['coord']
            self.side = 'left'
        if kwargs['side'] == 'k_right':
            self.x = kwargs['coord']
            self.side = 'right'
        if kwargs['side'] == 'k_up':
            self.y = kwargs['coord']
            self.side = 'up'
        if kwargs['side'] == 'k_buttom':
            self.y = kwargs['coord']
            self.side = 'buttom'
        add_object(self)


class User(SpriteParams):
    '''С помощью new мы имеем только один экземпляр класса'''
    __instance = None
    user_x = DISPLAY_SIZE[0] * 0.5
    user_y = DISPLAY_SIZE[1] * 0.5
    user_side = 'left'

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(User, cls).__new__(cls)
        return cls.__instance


class Mob(SpriteParams):
    ''' ширина и высота это постоянные переменные '''


class MobShot(SpriteParams):
    ''' Для этого класса нужно написать логику во views '''