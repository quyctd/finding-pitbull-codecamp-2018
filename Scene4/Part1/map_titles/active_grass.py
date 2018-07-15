from Scene4.game_object4_1 import GameObject
from Scene4.renderer.image_redenrer import ImageRenderer
from Scene4.box_collider import BoxCollider
import pygame

class Active_Grass(GameObject):
    def __init__(self,x , y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer('Scene4/images/map/grass1.png')
        # self.image = pygame.image.load('../images/map/grass1.png')
        self.collider = BoxCollider(32, 32)
        self.isActive = False
        self.Active = False
        self.count = 176
        self.limit = 416

    def update(self):
        GameObject.update(self)
        if self.x <= 138:
            self.Active = True
        if self.Active:
            self.run()
        if self.count >= self.limit:
            self.isActive = True

    def run(self):
        if self.count < self.limit:
            self.count +=8

