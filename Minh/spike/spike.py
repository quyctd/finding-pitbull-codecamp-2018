import pygame
from Minh.game_object import GameObject
from Minh.game_object import collide_with
from Minh.player.player import Player
from Minh.physics.box_collider import BoxCollider


class Spike(GameObject):

    def __init__(self, x, y, image):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load(image)
        self.box_collider = BoxCollider(28, 28, self)

    def update(self):
        collide_list = collide_with(self.box_collider)
        for obj in collide_list:
            if type(obj) == Player:
                obj.die = True
                break
