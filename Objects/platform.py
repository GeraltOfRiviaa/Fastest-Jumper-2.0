import pygame
from Objects.object import Object
from os import listdir
from os.path import join, isfile

class Platform(Object):
    """
    Used for all objects the player can move on without special things happening to him
    """
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, game)
        block = self.load_image(width,height, "Terrain.png",96,0, True,"Terrain" )
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)
        
    