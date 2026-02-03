import pygame
from Objects.object import Object
from os import listdir
from os.path import join, isfile

class Trophy(Object):
    def __init__(self, x, y,width, height, game, name=None):
        super().__init__(x,y,width,height,game,"trophy")
        trophy = self.load_image(width, height, "End (Idle).png", 0,0, "Items", "Checkpoints", "End")
        self.image.blit(trophy, (0,0))
        self.mask = pygame.mask.from_surface(self.image)
        
        #C:\Users\SAM\Desktop\Fastest Jumper 2.0\assets\Items\Checkpoints\End\End (Idle).png