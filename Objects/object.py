import pygame
from os import listdir
from os.path import join, isfile

class Object(pygame.surface.Surface):
    def __init__(self, x, y, width, height,game, name=None ):
        super().__init__((width, height))
        self.color = (255,0,0)
        self.rect = pygame.Rect(x,y,width,height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.name = name
        self.game = game
        self.x = x
        self.y = y
        self.spawn_x = x
        self.spawn_y = y
        self.animation_count = 0
    
    def draw(self):
        """Empty function used for drawing the object
        """
        self.game.window.blit(self.image, (self.rect.x , self.rect.y))
    
    def load_sprite_sheets(self, width, height, direction=False, scale = True, *directory):
        """Takes a spritesheet and creates Sprites from each square it selects based on width and height.
        Two directories are taken in this project, because of the structure

        Args:
            directory1 (string): first directory 
            directory2 (string, optional): second directory
            width (int): width of the sprite
            height (int): height of the sprite
            direction (bool, optional): True if directions are needed. Defaults to False.

        Returns:
            dict: names of the images and their surfaces
        """
        path = join("assets", *directory)
        images = [file for file in listdir(path) if isfile(join(path, file))]
        
        all_sprites = {}
        
        for image in images:
            sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
            sprites = []
            for i in range(sprite_sheet.get_width() // width):
                surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
                rect = pygame.Rect(i * width, 0, width, height)
                surface.blit(sprite_sheet, (0,0), rect)
                
                if scale:
                    sprites.append(pygame.transform.scale2x(surface))
                else:
                    sprites.append(surface)

            if direction:
                all_sprites[image.replace(".png", "") + "_right"] = sprites
                all_sprites[image.replace(".png", "") + "_left"] = self.flip(sprites)
            else:
                all_sprites[image.replace(".png", "")] = sprites
                
            
        return all_sprites
    
    def flip(self, sprites):
        """Flips the sprite by 180 

        Args:
            sprites (list): list of sprites in the animation
        """
        return[pygame.transform.flip(sprite, True,  False) for sprite in sprites]
    def update_sprite(self):
        """Empty function used to update sprites of an object
        """
        pass
    
    def load_image(self, width, height, name ,  position_x, position_y ,scale2x = True, *directory, ):
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
        
        path = join("assets", *directory, name)
        image = pygame.image.load(path).convert_alpha()
        surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
        rect = pygame.Rect(position_x, position_y, width, height)
        surface.blit(image, (0,0), rect)
        
        if scale2x:
            return pygame.transform.scale2x(surface)
        else:
            return surface
        