import pygame
from settings import PLATFORM_SIZE, HEIGHT_SCREEN
from Objects.platform import Platform
from Objects.fire import Fire
from Objects.trophy import Trophy


class Level_One():
    def __init__(self, game):
        self.game = game
        self.window = game.window
        
    def load_level_assets(self):
        background, background_image = self.game.get_background("Yellow.png")
        
        fires = [Fire((8 * PLATFORM_SIZE) + 51 , HEIGHT_SCREEN - PLATFORM_SIZE - 64, 16 ,32, self), # 8x 2y
                 Fire((9 * PLATFORM_SIZE) + 51 , HEIGHT_SCREEN - PLATFORM_SIZE - 64, 16 ,32, self), # 9x 2y
                 Fire((3 * PLATFORM_SIZE), HEIGHT_SCREEN - (PLATFORM_SIZE * 3) - 64, 16 ,32, self),
                 Fire((2 * PLATFORM_SIZE), HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self)
                
                ] 
        for fire in fires:
            fire.on()
        
        floor = [Platform( 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((1 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((2 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((3 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((7 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((8 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((9 * PLATFORM_SIZE ) + 20, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                ]
        #-WIDTH_SCREEN // PLATFORM_SIZE, WIDTH_SCREEN * 2 // PLATFORM_SIZE
        
        
        #creating individual platforms that make up a level
        floating_platforms = [Platform(2 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 3), PLATFORM_SIZE, PLATFORM_SIZE, self),# 3x 3y
                              Platform(3 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 3), PLATFORM_SIZE, PLATFORM_SIZE, self), # 4x 3y
                              Platform(6 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self), # 6x 4y
                              Platform(7 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self), # 7x 4y
                              Platform(1 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 6), PLATFORM_SIZE, PLATFORM_SIZE, self), # 2x 3y
                              Platform(2 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 6), PLATFORM_SIZE, PLATFORM_SIZE, self), # 3x 3y
                              Platform(6 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE, PLATFORM_SIZE, self), # 6x 7y
                              Platform(7 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE, PLATFORM_SIZE, self) # 6x 7y
                            ]
        
        #for testing use this:trophy = Trophy((2 * PLATFORM_SIZE),HEIGHT_SCREEN - (PLATFORM_SIZE * 2) + (64/2), 64,64, self)
        trophy = Trophy((7 * PLATFORM_SIZE) + 16,HEIGHT_SCREEN - (PLATFORM_SIZE * 8) + (64/2), 64,64, self)
        #trophy = Trophy((2 * PLATFORM_SIZE),HEIGHT_SCREEN - (PLATFORM_SIZE * 2) + (64/2), 64,64, self)
        objects = [*floor, *fires, *floating_platforms, trophy]
        
        return objects, background, background_image, fires