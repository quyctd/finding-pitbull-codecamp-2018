import pygame


class InputManager:

    def __init__(self, player):
        self.player = player
        self.s_pressed = False
        self.a_pressed = False
        self.d_pressed = False

    def update(self, event):
        dx = 0
        dy = 0
        step = 5
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.d_pressed = True
            elif event.key == pygame.K_a:
                self.a_pressed = True
            elif event.key == pygame.K_w:
                dy -= step
                self.player.jump_y = self.player.y
            elif event.key == pygame.K_s:
                dy += step
                self.player.jump_y = -1000000
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                self.d_pressed = False
            elif event.key == pygame.K_a:
                self.a_pressed = False
        if self.a_pressed:
            dx -= step
            self.player.image = "left"
        if self.d_pressed:
            dx += step
            self.player.image = "right"
        self.player.x += dx
        self.player.y += dy
