import pygame

class Timer():
    def __init__(self, game):
        self.game = game
        self.start_time = 0
        self.current_time = 0
        self.active = False
        self.delay = 0
    def start(self):
        self.active = True
        self.start_time = pygame.time.get_ticks() / 1000
    def proceed(self):
        self.active = True
        self.start_time = self.current_time
    def deactivate(self):
        self.active = False
        self.start_time = 0
        self.current_time = 0
        self.delay = 0
    def stop(self):
        self.active = False
        self.delay += self.current_time - self.start_time
        return self.delay
    def update(self):
        if self.active:
            self.current_time = pygame.time.get_ticks()/1000

    def pause(self):
        self.active = False
        self.delay = self.current_time - self.start_time