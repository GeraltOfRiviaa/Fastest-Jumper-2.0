import pygame
from os import listdir
from os.path import join, isfile
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, FPS
from Menus.font import Font
from Menus.button import Button


class Menu():
    def __init__(self, game):
        self.game = game
        
        self.image = pygame.Surface((WIDTH_SCREEN, HEIGHT_SCREEN)).convert_alpha()
        self.color = pygame.Color(0,0,0)
        self.image.fill(self.color)
        self.h1_font = Font(self.game, 10)
        self.h2_font = Font(self.game, 5)
        self.buttons = self.load_buttons()
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
        
    def display_text(self, text, x, y, size):
        """
        Displays a text on the screen
        """
        match size:
            case "h1":
                i = 0
                for letter in text.lower():
                    self.game.window.blit(self.h1_font.letters[letter], (x + (80*i),y))
                    i += 1
            case "h2":
                i = 0
                for letter in text.lower():
                    self.game.window.blit(self.h2_font.letters[letter], (x + (40*i),y))
                    i += 1

    def resolve_buttons(self):
        """Resolves all button presses
        """
        for _ in self.buttons:
            if self.buttons["Close.png"].pressed():
                self.game.running = False
                self.game.soundboard.click()
            if self.buttons["Volume.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Back.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Achievements.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Levels.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Next.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Play.png"].pressed():
                self.game.menu_state = "play"
                self.game.buttons = None
                self.game.soundboard.click()
                self.game.timer.start()
                if self.game.soundboard.music_paused:
                            self.game.soundboard.music_resume()
                            self.game.soundboard.music_paused = False
            if self.buttons["Previous.png"].pressed():
                self.game.soundboard.click()
            if self.buttons["Restart.png"].pressed():
                self.game.menu_state = "play"
                self.game.player.reset()
                self.game.buttons = None
                self.game.soundboard.click()
                self.game.soundboard.music_on()
                self.game.soundboard.reset()
                self.game.timer.start()
            if self.buttons["Settings.png"].pressed():
                self.game.soundboard.click()
    def load_buttons(self):
        """Loads every button in the game
        """
        path_one = "C:/Users/SAM/Desktop/Fastest Jumper 2.0/assets/Menu/Buttons"
        buttons = {} 
        for file in listdir(path_one) :
            if isfile(join(path_one, file)):
                buttons[file] =  Button(0,0, self.load_image(21,22, file,0,0, 3,"Menu", "Buttons"), self.game)

        path_two = "C:/Users/SAM/Desktop/Fastest Jumper 2.0/assets/Menu/Buttons/Smaller"
        for file in listdir(path_two) :
            if isfile(join(path_two, file)):
                buttons[file] =  Button(0,0, self.load_image(21,22, file,0,0, 2,"Menu", "Buttons", "Smaller"), self.game)
            

        return buttons