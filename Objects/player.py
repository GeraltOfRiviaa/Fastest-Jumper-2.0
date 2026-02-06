import pygame
from Objects.object import Object
from os import listdir
from os.path import join, isfile
from settings import GRAVITY,FPS, ANIMATION_DELAY, JUMP_STRENGTH, PLAYER_HEIGHT, PLAYER_WIDTH

class Player(Object):
    def __init__(self, x, y, width, height, game):
        super().__init__(x, y, width, height, game)
        self.velocity_x = 0
        self.velocity_y = 0
        self.mask = None
        self.direction = "left"
        
        self.fall_count = 0
        self.sprites = self.load_sprite_sheets( PLAYER_WIDTH,PLAYER_HEIGHT, True,True, "MainCharacters", "VirtualGuy")
        #self.dissapear_sprites = self.load_sprite_sheets(96,96, False, False ,"MainCharacters")
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        #self.dissapear_count = 0
        #self.dissapear = False
        
    def jump(self):
        self.velocity_y = -GRAVITY * JUMP_STRENGTH
        self.animation_count = 0
        self.jump_count += 1
        if self.jump_count == 1:
            self.fall_count = 0
    
    def move(self, velocity_x, velocity_y):
        """Moves the player based on velocity

        Args:
            velocity_x (int/float/double): speed of the player on x axes
            velocity_y (int/float/double): speed of the player on y axes
        """
        self.rect.x += velocity_x
        self.rect.y += velocity_y
        
    def move_left(self, velocity):
        """Changes the velocity of the player and the direction he's facing

        Args:
            velocity (int/float/double): speed of the player
        """
        if self.game.player_hits <= 2 and self.game.player_won == False:
            self.velocity_x = -velocity
            if self.direction != "left":
                self.direction = "left"
                self.animation_count = 0
            
    def move_right(self, velocity):
        """Changes the velocity of the player and the direction he's facing

        Args:
            velocity (int/float/double): speed of the player
        """
        if self.game.player_hits <= 2 and self.game.player_won == False:
            self.velocity_x = velocity
            if self.direction != "right":
                self.direction = "right"
                self.animation_count = 0
    
    def loop(self):
        """Applies the gravity and updates movement and sprites for the Player()
        """
        
        self.velocity_y += min(1, (self.fall_count/ FPS) * GRAVITY)
        
        self.move(self.velocity_x,self.velocity_y)
        
        self.fall_count += 1
        
        if self.hit:
            self.hit_count += 1
        
        if self.hit_count > 45:
            self.hit = False
            self.hit_count = 0
            
        self.update_sprite()
    
    def draw(self):
        """Draws the sprite of the player on screen
        """
        self.game.window.blit(self.sprite, (self.rect.x, self.rect.y))
        
    def update_sprite(self):
        """Updates the sprites direction and type of the player
        """
        sprite_sheet = "idle"
        
        
        if self.hit:
            sprite_sheet = "hit"
        elif self.velocity_y < 0:
            if self.jump_count == 1:
                sprite_sheet = "jump"
            elif self.jump_count == 2:
                sprite_sheet = "double_jump"
        elif self.velocity_y > GRAVITY * 2:
            sprite_sheet = "fall"
        elif self.velocity_x != 0:
            sprite_sheet = "run"
        #if self.dissapear:
        #    sprite_sheet = "Desappearing (96x96)"
        #    sprite_sheet_name = sprite_sheet
        #    sprites = self.dissapear_sprites[sprite_sheet_name]
        #else:
        #    
        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.sprites[sprite_sheet_name]
        sprite_index = (self.animation_count // ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()
        
    def update(self):
        """Updates the rect and mask based on the player current position
        """
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)
        
    def landed(self):
        self.fall_count = 0
        self.velocity_y = 0
        self.jump_count = 0
    
    def hit_head(self):
        self.count = 0
        self.velocity_y *= -1
    
    def hit_self(self):
        self.hit = True
        self.hit_count = 0
        
    def reset(self):
        super().reset()
        self.animation_count = 0
        self.direction = "right"
        self.jump_count = 0
        self.fall_count = 0
        self.velocity_x = 0
        self.velocity_y = 0