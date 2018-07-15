import pygame
from Minh.game_object import GameObject
from Minh.physics.box_collider import BoxCollider
from Minh.game_object import collide_with
from Minh.player.player import Player


class OneSideObject1(GameObject):

    def __init__(self, x, y, gravity):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("Minh/data/images/wall.png")
        self.box_collider = BoxCollider(42, 42, self)
        self.gravity = gravity
