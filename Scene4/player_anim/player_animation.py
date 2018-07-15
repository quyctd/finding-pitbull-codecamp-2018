from Scene4.renderer.animation import Animation
import pygame
from Scene4.renderer.image_redenrer import ImageRenderer

class PlayerAnimation:
    def __init__(self):
        self.left_animation = Animation(["Scene4/images/player/player_stand_left.png",
                                         "Scene4/images/player/player_walk2_left.png",
                                         "Scene4/images/player/player_walk1_left.png",
                                         "Scene4/images/player/player_walk2_left.png"],
                                        loop=True)
        self.right_animation = Animation(["Scene4/images/player/player_stand.png",
                                          "Scene4/images/player/player_walk2.png",
                                          "Scene4/images/player/player_walk1.png",
                                          "Scene4/images/player/player_walk2.png"],
                                         loop=True)
        self.jump_animation = Animation(["Scene4/images/player/player_stand.png",
                                         "Scene4/images/player/player.png",
                                         "Scene4/images/player/player_jump.png",
                                         "Scene4/images/player/player.png"],
                                        loop=True)
        self.jump_left_animation = Animation(["Scene4/images/player/player_stand_left.png",
                                         "Scene4/images/player/player_left.png",
                                         "Scene4/images/player/player_jump_left.png",
                                         "Scene4/images/player/player_left.png"],
                                        loop=True)
        self.straight_animation = ImageRenderer("Scene4/images/player/player_stand.png")
        self.left = ImageRenderer("Scene4/images/player/player_stand_left.png")
        self.current_animation = self.straight_animation

    def render(self, canvas, x, y):
        self.current_animation.render(canvas, x, y)

    def update(self, player_x, player_y):
        if player_x < 0:
            self.current_animation = self.left_animation
        elif player_x > 0:
            self.current_animation = self.right_animation
        elif player_y > 0:
            if self.current_animation == self.left or self.current_animation == self.left_animation or self.current_animation == self.jump_left_animation:
                self.current_animation = self.jump_left_animation
            else:
                self.current_animation = self.jump_animation
        else:
            if self.current_animation == self.left_animation or self.current_animation == self.jump_left_animation:
                self.current_animation = self.left
                # print(1)
            elif self.current_animation == self.right_animation:
                self.current_animation = self.straight_animation
            elif self.current_animation is not self.left:
                self.current_animation = self.straight_animation


