import pygame
from os import listdir
from os.path import join, isfile

class Soundboard():
    def __init__(self, game):
        self.game = game
        self.sounds = self.load_sounds()
        pygame.mixer.music.load("C:/Users/SAM/Desktop/Fastest Jumper 2.0/Music/track1.mp3")
        pygame.mixer.music.set_volume(0.5)
        self.game_over_played = False
        self.trophy_played = False
        
    def load_sounds(self):
        path = "C:/Users/SAM/Desktop/Fastest Jumper 2.0/Sound_Effects/WAV"
        sounds = {}
        for sound in listdir(path):
            if isfile(join(path, sound)):
                sounds[sound] = pygame.mixer.Sound(join(path, sound))
        return sounds
    
    def set_volume_all(self, volume):
        for sound in self.sounds:
            self.sounds[sound].set_volume(volume)
    
    def set_volume(self, sound, volume):
        self.sounds[sound].set_volume(volume)
    
    def click(self):
        self.sounds["click2.wav"].play()
    
    def game_over(self):
        self.sounds["game_over.wav"].play()
    
    def jump_landing(self):
        self.sounds["jump_landing_short.wav"].play()
    
    def jump(self):
        self.sounds["jump2.wav"].play()
        
    def trophy(self):
        self.sounds["trophy.wav"].play()
    def running(self):
        self.sounds["running.wav"].play()
    def music_off(self):
        #pygame.mixer.music.stop()
        pass
    def music_on(self):
        pass
        #pygame.mixer.music.play()
    def reset(self):
        self.game_over_played = False
        self.trophy_played = False