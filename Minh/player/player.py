import pygame
from Minh.physics.box_collider import BoxCollider
from Minh import game_object
from Minh.player.player_animation import PlayerAnimation


class Player:

    def __init__(self, x, y, background):
        self.x = x
        self.y = y
        self.display = True
        self.dir_x = 0
        self.dir_y = 0
        self.img_left = pygame.image.load("Minh/data/images/left.png")
        self.img_right = pygame.image.load("Minh/data/images/right.png")
        self.image = "right"
        self.box_collider = BoxCollider(36, 64, self)
        self.jump_time = 0
        self.die = False
        self.death_time = 0
        self.win = False
        self.background = background
        self.can_jump = False
        self.animation = PlayerAnimation()
        self.animation_active = False

    def activate(self):
        collide_list = game_object.collide_with(self.box_collider)
        for obj in collide_list:
            if type(obj) != Player:
                obj.activate()
                obj.update()

    def render(self, canvas):
        if not self.animation_active:
            self.image = "svsd"
        self.animation.update(self.image)
        self.animation.render(canvas, self.x, self.y)
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)

    def impact(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x + self.img_right.get_width() / 2
            self.box_collider.y = self.y + self.img_right.get_height() / 2

    def update(self):
        if self.die:
            return None
        self.x += self.dir_x * 2
        self.y += self.dir_y * 2
        if self.background is not None:
            if self.x < self.background.x:
                self.x = self.background.x
            if self.y < self.background.y:
                self.y = self.background.y
            if int(self.x) > int(self.background.x) + 1642:
                self.x = int(self.background.x) + 1642
            if int(self.y) > int(self.background.y) + 1470:
                self.y = int(self.background.y) + 1470
