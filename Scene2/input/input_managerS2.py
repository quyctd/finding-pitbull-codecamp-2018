import pygame
from Scene2.player.playerS2 import Player
class InputManager:
    def __init__(self):
        self.right_pressed = False
        self.left_pressed = False
        self.down_pressed = False
        self.up_pressed = False

    def __str__(self):
        return '''right: {0} left: {1} down: {2} up: {3}'''.format(
            self.right_pressed,
            self.left_pressed,
            self.down_pressed,
            self.up_pressed,

        )

    def update(self, event):
        isJump = False
        jumpCount = 10
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = True
            elif event.key == pygame.K_DOWN:
                self.down_pressed = True
            elif event.key == pygame.K_LEFT:
                self.left_pressed = True
            elif event.key == pygame.K_UP:
                self.up_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right_pressed = False
            elif event.key == pygame.K_DOWN:
                self.down_pressed = False
            elif event.key == pygame.K_LEFT:
                self.left_pressed = False
            elif event.key == pygame.K_UP:
                self.up_pressed = False

global_input_manager = InputManager()