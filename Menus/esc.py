import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, WORD_SPACING
from Menus.menu_template import Menu
from Menus.button import Button


class ESC(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.image.set_alpha(200)
        self.close = self.buttons["Close.png"]
        self.close.rect.topleft = (0,0)
        self.play = self.buttons["Play.png"]
        self.play.rect.topleft = (WIDTH_SCREEN/2,HEIGHT_SCREEN/2 + 21)
        self.volume = self.buttons["Volume.png"]
        self.volume.rect.topleft = (1000 - (21 * 3),1)
        self.restart = self.buttons["Restart.png"]
        self.restart.rect.topleft = (WIDTH_SCREEN/2 - (3*21) ,HEIGHT_SCREEN/2 + 21)
        self.pressed = False
                        

    def draw(self):
        """
        Draws the ECS menu on the screen
        """
        self.game.window.blit(self.image, (0,0))
        self.close.draw(self.game.window)
        self.play.draw(self.game.window)
        self.restart.draw(self.game.window)
        self.display_text("you", (WIDTH_SCREEN/2) - (3.5*80) - 40 , 200, "h1")
        self.display_text("good?",(WIDTH_SCREEN/2) - (0.5 * 80), 200, "h1")

    def check_pressed(self):
        if self.pressed:
            self.pressed = False
            self.game.menu_state = "play"
            self.game.buttons = None
        else:
            self.game.buttons = "esc"
            self.pressed = True