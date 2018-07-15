from Scene2.game_objectS2 import GameObject
from Scene2.renderer.image_renderer import ImageRenderer


class Jet(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)
        self.renderer = ImageRenderer("Scene2/assets/images/sprite/jet0000.png")