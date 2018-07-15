import pygame
from pygame.locals import *


class Elevator:

    def __init__(self, x, y, collide, player):
        self.x = x
        self.y = y
        self.player = player
        self.image = pygame.image.load("Scene4/images/ele_img.png")
        self.collider = collide
        self.activate = False
        self.destination = None
        self.pressClose = False
        self.on = False

    def render(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

    def check_collide(self, collide_list):
        for obj in collide_list:
            if obj == self.player:
                self.on = True

    def update(self, canvas):
        loop = True
        PlayerPass = ""
        CorrectPass = "minhdz123"
        ffont = pygame.font.Font(None, 100)
        loop1 = True
        PlayerPass1 = ""
        while loop:
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop = False
                    loop1 = False
                    self.pressClose = True
                elif even.type == KEYDOWN:
                    if even.key == pygame.K_RETURN:
                        if PlayerPass == CorrectPass:
                            self.activate = True
                            loop = False
                        elif PlayerPass.lower() == "e":
                            loop = False
                            loop1 = False
                            self.on = False
                        else:
                            PlayerPass = ""
                            canvas.blit(pygame.image.load('Scene4/images/elevator.png'), (0, 0))
                    elif even.key is not pygame.K_BACKSPACE:
                        PlayerPass += even.unicode
                    else:
                        PlayerPass = PlayerPass[:-1]
                        canvas.blit(pygame.image.load('Scene4/images/elevator.png'), (0, 0))
                chu = ffont.render(PlayerPass, True, (255, 0, 0))
                exit_font = ffont.render("Press E to exit the elevator!", True, (255,255, 255))
                canvas.blit(chu, (300, 300))
                canvas.blit(exit_font, (300, 500))
            pygame.display.flip()


        while loop1:
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop1 = False
                    self.pressClose = True
                elif even.type == KEYDOWN:
                    if even.key == pygame.K_RETURN:
                        if PlayerPass1 == "1":
                            loop1 = False
                            self.destination = 1
                        elif PlayerPass1 == "2":
                            loop1 = False
                            self.destination = 2
                        elif PlayerPass1 == "3":
                            loop1 = False
                            self.destination = 3
                        else:
                            PlayerPass = ""
                            canvas.blit(pygame.image.load('Scene4/images/elevator_on.png'), (0, 0))
                    elif even.key is not pygame.K_BACKSPACE:
                        PlayerPass += even.unicode
                    else:
                        PlayerPass = PlayerPass[:-1]
                        canvas.blit(pygame.image.load('Scene4/images/elevator_on.png'), (0, 0))
                chu = ffont.render(PlayerPass, True, (255, 0, 0))
                canvas.blit(chu, (300, 300))
            pygame.display.flip()
