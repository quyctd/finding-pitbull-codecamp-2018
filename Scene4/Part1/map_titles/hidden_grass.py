from Scene4.game_object4_1 import GameObject
from Scene4.renderer.image_redenrer import ImageRenderer
from Scene4.box_collider import BoxCollider
import pygame


class Hidden_Grass(GameObject):
    def __init__(self,x , y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer('Scene4/images/map/grass1.png')
        # self.image = pygame.image.load('../images/map/grass1.png')
        self.collider = BoxCollider(32, 32)
        self.isActive = False

