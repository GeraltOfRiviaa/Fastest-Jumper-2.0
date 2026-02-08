import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN,  WORD_SPACING
from Menus.menu_template import Menu
from Menus.button import Button


class Start(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.background, self.background_image = self.game.get_background("Brown.png")
        self.close = self.buttons["Close.png"]
        self.close.rect.topleft = (0,0)
        self.play = self.buttons["Play.png"]
        self.play.rect.topleft = (WIDTH_SCREEN/2 - 21,HEIGHT_SCREEN/2 + 21)
        
    def draw(self):
        """
        Draws the death menu on the screen
        """
        for tile in self.background:
                self.game.window.blit(self.background_image,tile)
        self.close.draw(self.game.window)
        self.play.draw(self.game.window)
        self.display_text("Fastest", (WIDTH_SCREEN/2) - (4*WORD_SPACING) - 40 , 200, "h1")
        self.display_text("Jumper",(WIDTH_SCREEN/2) - (2*WORD_SPACING), 300, "h1")