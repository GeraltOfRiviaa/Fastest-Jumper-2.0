import pygame
from Objects.object import Object
from settings import ANIMATION_DELAY

class Fire(Object):
    def __init__(self, x, y, width, height, game ,name=None):
        super().__init__(x, y, width, height, game, "fire")
        self.fire = self.load_sprite_sheets(self.width, self.height ,False, True, "Traps", "Fire",)
        self.image = self.fire["off"][0]
        self.mask = pygame.mask.from_surface(self.image)
        
        self.animation_name = "off"
        
    def on(self):
        self.animation_name = "on"
    
    def off(self):
        self.animation_name = "off"
    
    def update_sprite(self):
        
        sprites = self.fire[self.animation_name]
        sprite_index = (self.animation_count //
                        ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)

        if self.animation_count // ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
        