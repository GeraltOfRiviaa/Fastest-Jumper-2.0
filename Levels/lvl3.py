
from settings import PLATFORM_SIZE, HEIGHT_SCREEN, WIDTH_SCREEN
from Objects.platform import Platform
from Objects.fire import Fire
from Objects.trophy import Trophy

#made using AI
class Lvl3():
    def __init__(self, game):
        self.game = game
        self.window = game.window
        
    def load_level_assets(self):
        background_image = self.game.get_background("Blue.png")  # Use Blue or Pink for variety
        
        fires = [
                # Bottom left fire (under left mid platform)
                Fire((1 * PLATFORM_SIZE) + 30, HEIGHT_SCREEN - (PLATFORM_SIZE * 4) - 64, 16, 32, self), 
                
                # Middle fire (on middle platform area)
                Fire((2 * PLATFORM_SIZE) + 30, HEIGHT_SCREEN - (PLATFORM_SIZE * 2) - 64, 16, 32, self),
                Fire((4 * PLATFORM_SIZE) + 30, HEIGHT_SCREEN - (PLATFORM_SIZE * 2) - 64, 16, 32, self),
                
                # Right side fire (between middle platforms)
                Fire((4 * PLATFORM_SIZE) + 15, HEIGHT_SCREEN - (PLATFORM_SIZE * 4) - 64, 16, 32, self),
                
                # Top middle fire (on upper right platform)
                Fire((7 * PLATFORM_SIZE) + 30, HEIGHT_SCREEN - (PLATFORM_SIZE * 5) - 64, 16, 32, self),
                ]
        
        for fire in fires:
            fire.on()
        
        # Floor platforms (bottom row)
        floor = [
                Platform(0, HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 5), HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                Platform((PLATFORM_SIZE * 9), HEIGHT_SCREEN - PLATFORM_SIZE, PLATFORM_SIZE, PLATFORM_SIZE, self),
                ]
        
        # Floating platforms based on your image
        floating_platforms = [
                                # Top left corner - Player spawn area (row 8 from bottom)
                                Platform(0, HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE , PLATFORM_SIZE, self),
                                Platform(PLATFORM_SIZE, HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE , PLATFORM_SIZE, self),
                                
                                # Tall vertical column (left-center, rows 5-8)
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 9), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 8), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 7), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 6), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 3), HEIGHT_SCREEN - (PLATFORM_SIZE * 5), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Middle left platform (row 5)
                                Platform(PLATFORM_SIZE, HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 2), HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Middle right platform (row 5)
                                Platform((PLATFORM_SIZE * 4), HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Upper middle platform (row 6)
                                Platform((PLATFORM_SIZE * 6), HEIGHT_SCREEN - (PLATFORM_SIZE * 6), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Upper right platform cluster (rows 4-5)
                                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - (PLATFORM_SIZE * 4), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - (PLATFORM_SIZE * 5), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Middle tier platforms (row 3-4)
                                Platform((PLATFORM_SIZE * 6), HEIGHT_SCREEN - (PLATFORM_SIZE * 3), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                                # Tall right column (rows 2-7)
                                
                                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - (PLATFORM_SIZE * 3), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                Platform((PLATFORM_SIZE * 7), HEIGHT_SCREEN - (PLATFORM_SIZE * 2), PLATFORM_SIZE, PLATFORM_SIZE, self),
                                
                            ]
        
        # Trophy at the end (far right, on floor)
        trophy = Trophy((9 * PLATFORM_SIZE), HEIGHT_SCREEN - (PLATFORM_SIZE ) - 64, 64, 64, self)
        
        # Combine all objects
        objects = [*floor, *floating_platforms, trophy, *fires]
        return objects, background_image, fires