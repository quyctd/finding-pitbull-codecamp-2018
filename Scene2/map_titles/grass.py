from Scene2.game_objectS2 import GameObject
from Scene2.renderer.image_renderer import ImageRenderer
from Scene2.physics.box_collider import BoxCollider


class Grass(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("Scene2/assets/images/sprite/grass0000.png")
        self.box_collider = BoxCollider(28, 28)
