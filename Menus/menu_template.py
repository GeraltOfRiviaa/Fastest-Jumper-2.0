import pygame
from os import listdir
from os.path import join, isfile
from settings import WIDTH_SCREEN, HEIGHT_SCREEN
from Menus.font import Font


class Menu():
    def __init__(self, game):
        self.game = game
        
        self.image = pygame.Surface((WIDTH_SCREEN, HEIGHT_SCREEN)).convert_alpha()
        self.color = pygame.Color(0,0,0)
        self.image.fill(self.color)
        self.font = Font(self.game, 10)
    
    def load_image(self, width, height, name ,  position_x, position_y ,scale, *directory, ):
        """Loads an image

        Args:
            size (int): size of each block
            name (string): name of the file
            position_x (int, optional): x position of the block on the sheet.
            position_y (int, optional): y position of the block on the sheet.
            *directory (tuple): directorys used to access the image

        Returns:
            Surface()
        """
        
        path = join("assets", *directory, name)
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(position_x, position_y, width, height)
        surface.blit(image, (0,0), rect)
        
        if scale:
            return pygame.transform.scale(surface, (width * scale, height * scale))
        else:
            return surface
        
    def display_text(self, text, x, y):
        """
        Displays a text on the screen
        """
        i = 0
        for letter in text.lower():
            self.game.window.blit(self.font.letters[letter], (x + (80*i),y))
            i += 1

    def resolve_buttons(self):
        """
        Resolves button presses
        """
        pass