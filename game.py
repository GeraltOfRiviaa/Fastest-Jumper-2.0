import pygame
from os import listdir
from os.path import join, isfile
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, FPS, PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_VELOCITY, PLATFORM_SIZE, SCROLL_AREA_WIDTH
from Objects.player import Player
from Objects.platform import Platform
from Objects.fire import Fire
from Objects.trophy import Trophy

class Game():
    """Basic game object, that other files can reference.
    All the basic loops, event handling happens here
    """
    def __init__(self):
        pygame.display.set_caption("Fastest Jumper")
        self.window = pygame.display.set_mode((WIDTH_SCREEN, HEIGHT_SCREEN))
        pygame.SCALED
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(60, 700, PLAYER_WIDTH, PLAYER_HEIGHT, self)
        self.offset_x = 0
        self.objects, self.background, self.background_image, self.fires = self.level_one()
        self.music = pygame.mixer.music.load("C:/Users/SAM/Desktop/Fastest Jumper 2.0/Music/track1.mp3")
        #self.music = pygame.mixer.music.play()
        
        
        
    def main(self):
        """Main game loop that sets the FPS for the game and calls all the handling functions,
        calls for the loop() in Player() and calls for draw()
        """
        while self.running:
            
            self.clock.tick(FPS)
            
            self.handle_events()
            self.player.loop()
            self.handle_move()
            self.draw()
            
            
            #Background scrolling
            #if ((self.player.rect.right - self.offset_x >= WIDTH_SCREEN - SCROLL_AREA_WIDTH) and self.player.velocity_x > 0) or (
            #   (self.player.rect.left - self.offset_x <= SCROLL_AREA_WIDTH) and self.player.velocity_x < 0):
            #   self.offset_x += self.player.velocity_x
            
    def handle_events(self):
        """Checks if certain events occured and acts upon them.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                    self.player.jump()

    def get_background(self, name):
        """Loads a square that contains the background image and
        and then returns the image and positions of each
        square used to fill the background

        Args:
            tiles(list): positions of the tiles
            image(Surface): image used to fill the background
        """
        #Loading the background image
        image = pygame.image.load(join("assets","Background" ,name))
        
        #Set the size based on the image
        _,_,width, height = image.get_rect()
        tiles = []
        
        #Calculation of how many tiles is needed to fill the screen and whats their position
        for i in range(WIDTH_SCREEN // width + 1):
            for j in range(HEIGHT_SCREEN // height + 1):
                position = (i * width, j * height)
                tiles.append(position)
        
        return tiles, image

    def draw(self):
        """Draws every asset in the game
        """
        for fire in self.fires:
            fire.update_sprite()
        
        for tile in self.background:
            self.window.blit(self.background_image,tile)
        
        for object in self.objects:
            object.draw()
        
        self.player.draw()
        pygame.display.update()
        
    def handle_move(self):
        """Handles all the movement of the player
        """
        keys = pygame.key.get_pressed()
        
        self.player.velocity_x = 0
        collide_left = self.handle_horizontal_collision( -PLAYER_VELOCITY * 2, self.objects)
        collide_right = self.handle_horizontal_collision( PLAYER_VELOCITY * 2 ,self.objects)
        
        
        if keys[pygame.K_a] and not collide_left:
            self.player.move_left(PLAYER_VELOCITY)
        if keys[pygame.K_d] and not collide_right:
            self.player.move_right(PLAYER_VELOCITY) 
        
        vertical_collide = self.handle_vertical_collision(self.player.velocity_y, self.objects)
        
        check = [collide_left, collide_right, *vertical_collide]
        
        for object in check:
            if object and object.name == "fire":
                self.player.hit_self()
                
            
    def handle_vertical_collision(self, velocity_y, objects):
        """Gives back a list of object the player collided with

        Args:
            velocity_y (int, double, float): velocity_y of player
            objects (list): objects we wanna check collision for

        Returns:
            list: list of object the player collided with
        """
        collided_objects = []
        for object in objects:
            if pygame.sprite.collide_mask(self.player, object):
                if velocity_y > 0:
                    self.player.rect.bottom = object.rect.top
                    self.player.landed()
                elif velocity_y < 0:
                    self.player.rect.top = object.rect.bottom
                    self.player.hit_head()
                    
                collided_objects.append(object)
        return collided_objects
    
    def handle_horizontal_collision(self, velocity_x, objects):
        """Moves the player to a position and checks if we are colliding with an object on that position.
        Returning the object the player collided with

        Args:
            velocity_y (int, float, double): velocity of the player
            objects (list): objects we wanna check for collision

        Returns:
            list: object we collide with
        """
        self.player.move(velocity_x, 0)
        self.player.update()
        collided_object = None
        for object in objects:
            if pygame.sprite.collide_mask(self.player, object):
                collided_object = object
                break
        
        self.player.move(-velocity_x, 0)
        self.player.update()
        
        return collided_object
    
    def level_one(self):
        
        background, background_image = self.get_background("Yellow.png")
        
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
                              Platform(6 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE, PLATFORM_SIZE, self), # 4x 3y
                              Platform(7 * PLATFORM_SIZE , HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE, PLATFORM_SIZE, self) # 4x 3y
                            ]
        
        #trophy = Trophy(7 * PLATFORM_SIZE,HEIGHT_SCREEN - (PLATFORM_SIZE * 8), 64,64, self)
        
        objects = [*floor, *fires, *floating_platforms]
        
        return objects, background, background_image, fires