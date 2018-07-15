import pygame
from Minh.game_object import GameObject
from Minh.physics.box_collider import BoxCollider


class Chest(GameObject):

    def __init__(self, x, y, image):
        GameObject.__init__(self, x, y)
        self.box_collider = BoxCollider(42, 42, self)
        self.image = pygame.image.load(image)
