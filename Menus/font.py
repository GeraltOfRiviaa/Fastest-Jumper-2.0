import pygame
import pygame
from os import listdir
from os.path import join, isfile

class Font():
    def __init__(self, game, scale):
        self.scale = scale
        self.game = game
        
        self.letter_cache = {}

        row_1 = self.get_font("abcdefghij",0)
        row_2 = self.get_font("klmnopqrst",10)
        row_3 = self.get_font("uvwxyz",20)
        row_4 = self.get_font("0123456789",30)
        row_5 = self.get_font(".,:?!()+-",40)

        self.letters = self.connect_letters(row_1,row_2,row_3,row_4,row_5)
        
    def load_image(self, width, height, name ,  position_x, position_y ,scale, *directory, ):
        """Loads the block we wanna use by using only one numbers as a size, because the assets are
        made that way

        Args:
            size (int): size of each block
            name (string): name of the file
            position_x (int, optional): x position of the block on the sheet.
            position_y (int, optional): y position of the block on the sheet.
            *directory (tuple): directorys used to access the image

        Returns:
            Surface()
        """
        cache_key = (width, height, name, position_x, position_y, scale, directory)
        if cache_key in self.letter_cache:
            return self.letter_cache[cache_key]
        
        path = join("assets", *directory, name)
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32).convert_alpha()
        rect = pygame.Rect(position_x, position_y, width, height)
        surface.blit(image, (0,0), rect)
        
        if scale:
            self.letter_cache[cache_key] = pygame.transform.scale(surface, (width * scale, height * scale))
            return pygame.transform.scale(surface, (width * scale, height * scale))
            
        else:
            self.letter_cache[cache_key] = surface
            return surface
            
    
    def get_font(self, text, y):
        letters = {}
        i = 0
        for letter in text:
            letters[letter] = self.load_image(8,10, "Text (White) (8x10).png" ,0 + (i * 8), y, self.scale, "Menu", "Text")
            i += 1
        return letters

    def connect_letters(self, *dictionarys):
        final_dictionary = {}
        for dictionary in dictionarys:
            final_dictionary.update(dictionary)

        return final_dictionary

