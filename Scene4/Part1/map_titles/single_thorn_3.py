from Scene4.game_object4_1 import GameObject
from Scene4.renderer.image_redenrer import ImageRenderer
from Scene4.box_collider import BoxCollider
import pygame


class SingleThorn_3(GameObject):
    def __init__(self,x , y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer('Scene4/images/trap/single_thorn_3.png')
        # self.image = pygame.image.load('../images/trap/medium_thorn.png')
        self.collider = BoxCollider(20, 124)
        self.limit = 416
        self.Active = False

    def update(self):
        GameObject.update(self)
        if self.x <= 138:
            self.Active = True
        if self.Active:
            self.run()

    def run(self):
        if self.y < self.limit:
            self.y +=8