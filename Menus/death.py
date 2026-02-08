import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, WORD_SPACING
from Menus.menu_template import Menu
from Menus.button import Button


class Death(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.image.set_alpha(200)

        self.close = self.buttons["Close.png"]
        self.close.rect.topleft = (0,0)
        self.restart = self.buttons["Restart.png"]
        self.restart.rect.topleft = (WIDTH_SCREEN/2 - 21,HEIGHT_SCREEN/2 + 21)
        
    def draw(self):
        """
        Draws the death menu on the screen
        """
        self.game.window.blit(self.image, (0,0))
        self.close.draw(self.game.window)
        self.restart.draw(self.game.window)
        self.display_text("You", (WIDTH_SCREEN/2) - (3*80) - 40 , 200, "h1")
        self.display_text("Died",(WIDTH_SCREEN/2), 200, "h1")

    