import pygame
from Objects.object import Object
from os import listdir
from os.path import join, isfile

class Platform(Object):
    """
    Used for all objects the player can move on without special things happening to him
    """
    def __init__(self, x, y, size, game):
        super().__init__(x, y, size, size, game)
        block = self.load_block(size)
        self.image.blit(block, (0,0))
        self.mask = pygame.mask.from_surface(self.image)
        
    def load_block(self, size, position_x = 96, position_y = 0):
        """Loads the block we wanna use by using only one numbers as a size, because the assets are
        made that way

        Args:
            size (int): size of each block
            position_x (int, optional): x position of the block on the sheet. Defaults to 96.
            position_y (int, optional): y position of the block on the sheet. Defaults to 0.

        Returns:
            Surface()
        """
        
        path = join("assets", "Terrain", "Terrain.png")
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        rect = pygame.Rect(position_x, position_y, size, size)
        surface.blit(image, (0,0), rect)
        return pygame.transform.scale2x(surface)