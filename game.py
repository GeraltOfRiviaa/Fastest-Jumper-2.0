import pygame
from os.path import join
import math
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, FPS, PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_VELOCITY, PLATFORM_SIZE, SCROLL_AREA_WIDTH
from Objects.player import Player
from Menus.death import Death
from Menus.win import Win
from Menus.start import Start
from Levels.lvl1 import Lvl1
from Levels.lvl2 import Lvl2
from Levels.lvl3 import Lvl3
from Menus.esc import ESC
from soundboard import Soundboard
from Menus.font import Font
from timer import Timer
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
        self.player = Player(60, HEIGHT_SCREEN - (PLATFORM_SIZE*2), PLAYER_WIDTH, PLAYER_HEIGHT, self)
        self.offset_x = 0
        self.death_menu = Death(self)
        self.start_menu = Start(self)
        self.win_menu = Win(self)
        self.level_one = Lvl1(self)
        self.level_two = Lvl2(self)
        self.level_three = Lvl3(self)
        self.esc_menu = ESC(self)
        self.objects, self.background, self.background_image, self.fires = self.level_one.load_level_assets()
        self.player_hits = 0
        self.buttons = "start"
        self.menu_state = "start"
        self.player_won = False
        self.soundboard = Soundboard(self)
        self.soundboard.set_volume_all(0.3)
        self.soundboard.set_volume("jump_landing_short.wav", 1)
        self.soundboard.set_volume("jump.wav", 0.1)
        self.time_saved = False
        self.sorted_death_times = []
        self.sorted_winning_times = []
        self.timer = Timer(self)
        self.start_time = 0
        self.font = Font(self, 3)
    def main(self):
        """Main game loop that sets the FPS for the game and calls all the handling functions,
        calls for the loop() in Player() and calls for draw()
        """
        while self.running:
            
            self.clock.tick(FPS)
            self.timer.update()
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
            pressed = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.player.jump_count < 2:
                    self.player.jump()
                if event.key == pygame.K_ESCAPE and self.menu_state == "play":
                        self.esc_menu.check_pressed()
                        if pressed:
                            self.timer.proceed()
                            pressed = False
                        else:
                            self.timer.stop()
                            pressed = True

            if self.buttons == "death":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.death_menu.resolve_buttons()
            if self.buttons == "start":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.start_menu.resolve_buttons()
            if self.buttons == "win":
                if event.type == pygame.MOUSEBUTTONDOWN:
                        self.win_menu.resolve_buttons()
            
            if self.buttons == "esc":
                if event.type == pygame.MOUSEBUTTONDOWN:            
                        self.esc_menu.resolve_buttons()
                        
            
            
    def get_background(self, name):
        """Loads a square that contains the background image
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
        
        
        if self.menu_state == "start":
            self.start_menu.draw()
        
        elif self.menu_state == "play":
            self.soundboard.music_on()
            for fire in self.fires:
                fire.update_sprite()
            
            for tile in self.background:
                self.window.blit(self.background_image,tile)
            
            for object in self.objects:
                object.draw()
            
            if self.player.rect.y > HEIGHT_SCREEN:
                if not self.time_saved:
                    self.save_time("death")
                    self.time_saved = True
                    self.sorted_death_times = self.sort_time(self.sort_death_time())

                self.buttons = "death"
                self.death_menu.draw()
                if not self.soundboard.game_over_played:
                    self.soundboard.game_over()
                    self.soundboard.game_over_played = True
                self.soundboard.music_off()
                self.display_timer(format(self.get_latest_time()), 1000 - (20 * 5.2),1)
            if self.player_hits > 2:
                if not self.time_saved:
                    self.save_time("death")
                    self.time_saved = True
                    self.sorted_death_times = self.sort_time(self.sort_death_time())
                    

                self.buttons = "death"
                self.death_menu.draw()
                if not self.soundboard.game_over_played:
                    self.soundboard.game_over()
                    self.soundboard.game_over_played = True
                self.soundboard.music_off()
                self.display_timer(format(self.get_latest_time()), 1000 - (20 * 5.2),1)
            
            if self.player_won:
                if not self.time_saved:
                    self.save_time("win")
                    self.time_saved = True
                    self.sorted_winning_times = self.sort_time(self.sort_win_time())
                    
                self.buttons = "win"
                self.win_menu.draw()
                self.soundboard.music_off()
                if not self.soundboard.trophy_played:
                    self.soundboard.trophy()
                    self.soundboard.trophy_played = True 
            
            if self.buttons == "esc":
                
                self.esc_menu.draw()
                self.display_timer(format(self.timer.current_time), 1000 - (20 * 5.2),1)
            if self.buttons == "death" or self.buttons == "win" or self.buttons == "esc":
                self.sorted_winning_times = self.sort_time(self.sort_win_time())
            else:
                self.display_timer("{:.2f}".format(self.timer.current_time), 1000 - (20 * 5.2),1)
            self.player.draw()
            
            
        pygame.display.update()
        
        
    def handle_move(self):
        """Handles all the movement of the player
        """
        keys = pygame.key.get_pressed()
        
        self.player.velocity_x = 0
        
        collide_left, collide_right, *vertical_collide = self.collided()
        
        if keys[pygame.K_a] and not collide_left:
            self.player.move_left(PLAYER_VELOCITY)
        if keys[pygame.K_d] and not collide_right:
            self.player.move_right(PLAYER_VELOCITY) 
        
        
        
        check = [collide_left, collide_right, *vertical_collide]
        
        for object in check:
            if object and object.name == "fire":
                if collide_left:
                    self.player.move_right(40)
                    self.player.move(0,-40)
                if collide_right:
                    self.player.move_left(40)
                    pass
                self.player.hit_self()
                self.player_hits += 1
                
                    
            if object and object.name == "trophy":
                self.player_won = True
                
        
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

    def save_time(self, state):
        
        with open("run_times.txt", "a") as file:
            file.write("{:.2f}".format(self.timer.current_time) + " " + state)
            file.write("\n")
        

    def read_time(self):
        times = []
        temp = []
        string = ""
        with open("run_times.txt", "r") as file:
            #reads lines from the file and appends them to times list
            for char in file.read():
                if not char == '\n':
                    temp.append(char)
                    
                if char == '\n':
                    for char in temp:
                        string += char
                    times.append(string)
                    string = ""
                    temp.clear()
        return times
    
    def sort_win_time(self):
        times = self.read_time()
        win_times = []
        for time in times:
            if not time.find("win") == -1:
                temp = time.split(' ')
                string = temp[0]
                win_times.append(string)
                string = ""
        return win_times
    
    def sort_death_time(self):
        times = self.read_time()
        death_times = []
        for time in times:
            if not time.find("death") == -1:
                temp = time.split(' ')
                
                string = temp[0]
                death_times.append(string)
                string = ""
        return death_times
    
    def sort_time(self, times, ascending = True):
        if ascending:
            for i in range(len(times) - 1):
                swapped = False
                for j in range(len(times) - i - 1):
                    if times[j] > times[j+1]:
                        times[j], times[j+1] = times[j+1], times[j]
                        swapped = True
                if not swapped:
                    break
        else:
            for i in range(len(times) - 1):
                swapped = False
                for j in range(len(times) - i - 1):
                    if times[j] < times[j+1]:
                        times[j], times[j+1] = times[j+1], times[j]
                        swapped = True
                if not swapped:
                    break
        return times

    def collided(self):
        collide_left = self.handle_horizontal_collision( -PLAYER_VELOCITY * 2, self.objects)
        collide_right = self.handle_horizontal_collision( PLAYER_VELOCITY * 2 ,self.objects)
        vertical_collide = self.handle_vertical_collision(self.player.velocity_y, self.objects)
        collision = [collide_left, collide_right, *vertical_collide]
        return collision
    def get_latest_time(self):
        times = []
        for time in self.read_time():
                temp = time.split(' ')
                string = temp[0]
                times.append(string)
                string = ""
        return times[-1]
    
    def display_timer(self, text, x, y):
        """
        Displays a timer on the screen
        """
        
        i = 0
        for letter in text.lower():
            self.window.blit(self.font.letters[letter], (x + (20*i),y))
            i += 1
