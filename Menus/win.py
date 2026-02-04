import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN, WORD_SPACING
from Menus.menu_template import Menu
from Menus.button import Button


class Win(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.image.set_alpha(200)
        self.buttons = [Button((WIDTH_SCREEN/2) - 21,(HEIGHT_SCREEN/2) - 22, self.load_image(21,22, "Restart.png",0,0, 2,"Menu", "Buttons")),
                        Button(10,10, self.load_image(15,16, "Close.png",0,0, 3,"Menu", "Buttons")),
                        Button(900,30, self.load_image(21,22, "Volume.png",0,0, 3,"Menu", "Buttons"))]

    def draw(self):
        """
        Draws the death menu on the screen
        """
        self.game.window.blit(self.image, (0,0))
        i = 0
        for button in self.buttons:
            self.game.window.blit(button.image, (button.x, button.y))
            self.buttons[i].draw(self.game.window)
            i += 1
        self.display_text("You", (WIDTH_SCREEN/2) - (3*80) - 40 , 200)
        self.display_text("Won",(WIDTH_SCREEN/2), 200)

    def resolve_buttons(self):
            if self.buttons[1].pressed():
                self.game.running = False
            if self.buttons[0].pressed():
                self.game.menu_state = "play"
            if self.buttons[2].pressed():
                if self.game.music == True:
                    pygame.mixer.music.stop()
                    self.game.music = False
                elif self.game.music == False:
                    self.game.music = True
                    pygame.mixer.music.play()