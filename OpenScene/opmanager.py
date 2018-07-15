import pygame
from pygame.locals import *
from OpenScene.opening_animation import OpeningAnimation

class Main():
    def __init__(self, scene1):
        self.end = False
        self.pressClose = False
        self.scene1 = scene1
        self.opening = OpeningAnimation()


    def update(self, canvas):
        loop = True
        clock = pygame.time.Clock()
        numScene = 1
        player_name = ""
        ffont = pygame.font.Font("OpenScene/fonts/arial.ttf", 100)
        font1 = pygame.font.Font("OpenScene/fonts/arial.ttf", 50)
        pygame.mixer.music.load('OpenScene/fastbeat.wav')
        pygame.mixer.music.play(-1)

        while loop:
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop = False
                    self.pressClose = True
                elif even.type == KEYDOWN:
                    if numScene == 1:
                        if even.key == pygame.K_RETURN:
                            numScene += 1
                        elif even.key == pygame.K_ESCAPE:
                            loop = False
                            self.pressClose = True
                    elif numScene == 2:
                        if even.key == pygame.K_RETURN:
                            numScene += 1
                        elif even.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        else:
                            player_name += even.unicode
                        # chu = ffont.render(player_name, True, (255, 0, 0))
                        # canvas.blit(chu, (300, 300))
                    elif numScene > 2 and even.key == pygame.K_RETURN:
                        numScene += 1

            if numScene == 1:
                image = pygame.image.load('OpenScene/images/startgame.png')
                canvas.blit(image, (0, 0))
            elif numScene == 2:
                chu = ffont.render(player_name, True, (255, 0, 0))
                image = pygame.image.load('OpenScene/images/enter_name.jpg')
                canvas.blit(image, (0, 0))
                canvas.blit(chu, (300, 300))
            elif numScene == 5:
                self.scene1.update(canvas)
                numScene += 1
            elif numScene == 3:
                chu1 = font1.render(player_name, True, (0, 0, 0))
                image = pygame.image.load('OpenScene/images/story1.png')
                canvas.blit(image, (0, 0))
                canvas.blit(chu1, (220, 450))
            elif numScene == 4:
                image = pygame.image.load('OpenScene/images/story2.png')
                canvas.blit(image, (0, 0))
            elif numScene == 6:
                image = pygame.image.load('OpenScene/images/story3.png')
                canvas.blit(image, (0, 0))
            elif numScene == 7:
                self.opening.render(canvas, 0, 0)
                if self.opening.op_animation.allow:
                    numScene += 1
            elif numScene == 8:
                image = pygame.image.load('OpenScene/images/huongdan.png')
                canvas.blit(image, (0, 0))
            else:
                loop = False
                pygame.mixer.music.stop()
                self.end = True

            pygame.display.flip()
            clock.tick(60)
