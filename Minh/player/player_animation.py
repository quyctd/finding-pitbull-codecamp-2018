import pygame
from Minh.player.animation import Animation


class PlayerAnimation:

    def __init__(self):
        self.left_animation = Animation(["Minh/data/images/player/playerLeft1.png",
                                         "Minh/data/images/player/playerLeft2.png",
                                         "Minh/data/images/player/playerLeft3.png",
                                         "Minh/data/images/player/playerLeft4.png"],
                                        loop=True)
        self.right_animation = Animation(["Minh/data/images/player/player1.png",
                                          "Minh/data/images/player/playerWalk2.png",
                                          "Minh/data/images/player/playerWalk3.png",
                                          "Minh/data/images/player/playerWalk4.png"],
                                         loop=True)
        self.jump_animation = Animation(["Minh/data/images/player/player1.png",
                                         "Minh/data/images/player/playerJump1.png",
                                         "Minh/data/images/player/playerJump2.png",
                                         "Minh/data/images/player/playerJump3.png"],
                                        loop=True)
        self.jump_left_animation = Animation(["Scene4/images/player/player_stand_left.png",
                                              "Scene4/images/player/player_left.png",
                                              "Scene4/images/player/player_jump_left.png",
                                              "Scene4/images/player/player_left.png"],
                                             loop=True)
        self.straight_animation = pygame.image.load("Minh/data/images/player/player1.png")
        self.left = pygame.image.load("Minh/data/images/player/playerLeft1.png")
        self.death_animation = Animation(["Minh/data/images/player/player1.png", "Minh/data/images/player/playerDeath1.png",
                                "Minh/data/images/player/playerDeath2.png", "Minh/data/images/player/playerDeath3.png"], loop=True)
        self.current_animation = self.straight_animation

    def render(self, canvas, x, y):
        if self.current_animation == self.straight_animation or self.current_animation == self.left:
            canvas.blit(self.current_animation, (x, y))
        else:
            self.current_animation.render(canvas, x, y)

    def update(self, direction):
        if direction == "left":
            self.current_animation = self.left_animation
        elif direction == "right":
            self.current_animation = self.right_animation
        elif direction == "jump":
            if self.current_animation == self.left or self.current_animation == self.left_animation or self.current_animation == self.jump_left_animation:
                self.current_animation = self.jump_left_animation
            else:
                self.current_animation = self.jump_animation
        elif direction == "death":
            self.current_animation = self.death_animation
        else:

            if self.current_animation == self.right_animation or self.current_animation == self.jump_animation:
                self.current_animation = self.straight_animation
            elif self.current_animation == self.left_animation or self.current_animation == self.jump_left_animation:
                self.current_animation = self.left


