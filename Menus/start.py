import pygame
from settings import WIDTH_SCREEN, HEIGHT_SCREEN,  WORD_SPACING
from Menus.menu_template import Menu
from Menus.button import Button


class Start(Menu):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        self.background, self.background_image = self.game.get_background("Brown.png")
        self.buttons = [Button((WIDTH_SCREEN/2) - 63,((HEIGHT_SCREEN/2) + 100) - 66, self.load_image(21,22, "Play.png",0,0, 4,"Menu", "Buttons")),
                        Button(900,30, self.load_image(21,22, "Volume.png",0,0, 3,"Menu", "Buttons"))]
        
    
    def draw(self):
        """
        Draws the death menu on the screen
        """
        for tile in self.background:
                self.game.window.blit(self.background_image,tile)
        i = 0
        for button in self.buttons:
            self.game.window.blit(button.image, (button.x, button.y))
            self.buttons[i].draw(self.game.window)
            i += 1
        self.display_text("Fastest", (WIDTH_SCREEN/2) - (4*WORD_SPACING) - 40 , 200)
        self.display_text("Jumper",(WIDTH_SCREEN/2) - (2*WORD_SPACING), 300)

    def resolve_buttons(self):
            if self.buttons[0].pressed():
                self.game.menu_state = "play"
            if self.buttons[1].pressed():
                if self.game.music == True:
                    pygame.mixer.music.stop()
                    self.game.music = False
                elif self.game.music == False:
                    self.game.music = True
                    pygame.mixer.music.play()