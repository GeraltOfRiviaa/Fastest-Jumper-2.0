import pygame
from settings import PLATFORM_SIZE, HEIGHT_SCREEN
from Objects.platform import Platform
from Objects.fire import Fire
from Objects.trophy import Trophy


class Lvl2():
    def __init__(self, game):
        self.game = game
        self.window = game.window
    def load_level_assets(self):
        background_image = self.game.get_background("Green.png")
        
        fires = [
                #line 3 
                Fire((5 * PLATFORM_SIZE), HEIGHT_SCREEN - (PLATFORM_SIZE * 2) - 64, 16 ,32, self), 
                #lie  5
                Fire((2* PLATFORM_SIZE) , HEIGHT_SCREEN - (PLATFORM_SIZE * 4) - 64, 16 ,32, self),
                #line 6
                Fire(51 , HEIGHT_SCREEN - (PLATFORM_SIZE * 5) - 64, 16 ,32, self,90), 
                #line 7
                Fire((4 * PLATFORM_SIZE) + (51) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self), 
                Fire((4 * PLATFORM_SIZE) + (21) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self), 
                Fire((5 * PLATFORM_SIZE) + (51) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self), 
                Fire((5 * PLATFORM_SIZE) + (21) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self),
                Fire((6 * PLATFORM_SIZE) + (51) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self), 
                Fire((6 * PLATFORM_SIZE) + (21) , HEIGHT_SCREEN - (PLATFORM_SIZE * 6) - 64, 16 ,32, self),
                ]
        for fire in fires:
            fire.on()
        
        floor = [
                Platform(0, HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 1), HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 5), HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 8), HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 9), HEIGHT_SCREEN - PLATFORM_SIZE,PLATFORM_SIZE, PLATFORM_SIZE, self),
                ]
        #-WIDTH_SCREEN // PLATFORM_SIZE, WIDTH_SCREEN * 2 // PLATFORM_SIZE
        
        
        #creating individual platforms that make up a level
        floating_platforms = [
                                #line 2
                                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - (PLATFORM_SIZE * 2),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                #line 3
                                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - (PLATFORM_SIZE * 3),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 4), HEIGHT_SCREEN - (PLATFORM_SIZE * 3),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - (PLATFORM_SIZE * 3),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 8), HEIGHT_SCREEN - (PLATFORM_SIZE * 3),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 9), HEIGHT_SCREEN - (PLATFORM_SIZE * 3),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                #line 4
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 4),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                #line 5
                                Platform(0, HEIGHT_SCREEN - (PLATFORM_SIZE * 5),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 1), HEIGHT_SCREEN - (PLATFORM_SIZE * 5),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 4), HEIGHT_SCREEN - (PLATFORM_SIZE * 5),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                #line 6
                                Platform((PLATFORM_SIZE * 4), HEIGHT_SCREEN - (PLATFORM_SIZE * 6),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 5), HEIGHT_SCREEN - (PLATFORM_SIZE * 6),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 6), HEIGHT_SCREEN - (PLATFORM_SIZE * 6),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 8), HEIGHT_SCREEN - (PLATFORM_SIZE * 6),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 9), HEIGHT_SCREEN - (PLATFORM_SIZE * 6),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                #line 7
                                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - (PLATFORM_SIZE * 7),PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 7),PLATFORM_SIZE, PLATFORM_SIZE, self),
                            ]
        
        #for testing use this:trophy = Trophy((2 * PLATFORM_SIZE),HEIGHT_SCREEN - (PLATFORM_SIZE * 2) + (64/2), 64,64, self)
        trophy = Trophy((9 * PLATFORM_SIZE) + 16,HEIGHT_SCREEN - (PLATFORM_SIZE * 2) + (64/2), 64,64, self)
        #trophy = Trophy((2 * PLATFORM_SIZE),HEIGHT_SCREEN - (PLATFORM_SIZE * 2) + (64/2), 64,64, self)
        objects = [*floor, *fires, *floating_platforms, trophy]
        
        
        
        return objects, background_image, fires