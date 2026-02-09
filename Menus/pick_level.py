import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN,  WORD_SPACING
from Menus.menu_template import Menu



class Pick_Level(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.background_image = self.game.get_background("Brown.png")
        self.close = self.buttons["Close.png"]
        self.close.rect.topleft = (1000 - (1 + 38), 1)
        
        self.lvl1 = self.buttons["01.png"]
        self.lvl1.rect.topleft = (((WIDTH_SCREEN/2) - 15) - (2 * 30),500 )
        
        self.lvl2 = self.buttons["02.png"]
        self.lvl2.rect.topleft = ((WIDTH_SCREEN/2) - 15, 500)
        
        self.lvl3 = self.buttons["03.png"]
        self.lvl3.rect.topleft = (((WIDTH_SCREEN/2) - 15) + (2 * 30),500)
        
        self.back = self.buttons["Back.png"]
        self.back.rect.topleft = (0,0)
    def draw(self):
        """
        Draws the death menu on the screen
        """
        self.game.window.blit(self.background_image,(0,0))
        self.lvl1.draw(self.game.window)
        self.lvl2.draw(self.game.window)
        self.lvl3.draw(self.game.window)
        self.back.draw(self.game.window)
        self.close.draw(self.game.window)
        self.display_text("Pick", (WIDTH_SCREEN/2) - (4*WORD_SPACING) - 40 , 200, "h1")
        self.display_text("Your", (WIDTH_SCREEN/2) - (2*WORD_SPACING) - 40 , 300, "h1")
        self.display_text("Level",(WIDTH_SCREEN/2) - (0*WORD_SPACING), 400, "h1")