import pygame
from settings import PLATFORM_SIZE, HEIGHT_SCREEN
from Objects.platform import Platform
from Objects.fire import Fire
from Objects.trophy import Trophy


class Lvl3():
    def __init__(self, game):
        self.game = game
        self.window = game.window
        
    