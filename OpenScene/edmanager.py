import pygame
from pygame.locals import *
from OpenScene.ending_animation import EndingAnimation

class Main():
    def __init__(self):
        self.end = False
        self.pressClose = False
        self.ending = EndingAnimation()


    def update(self, canvas):
        loop = True
        clock = pygame.time.Clock()
        pygame.mixer.music.load('OpenScene/fastbeat.wav')
        pygame.mixer.music.play(-1)

        while loop:
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop = False
                    self.pressClose = True

            self.ending.render(canvas,0, 0)

            pygame.display.flip()
            clock.tick(60)
