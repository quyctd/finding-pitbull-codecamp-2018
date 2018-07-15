import pygame
from Minh.player.animation import Animation


class GateAnimation:

    def __init__(self):
        self.gate_ani = Animation(["Minh/data/images/teleport/door.png",
                                    "Minh/data/images/teleport/door1.png",
                                    "Minh/data/images/teleport/door2.png",
                                    "Minh/data/images/teleport/door3.png",
                                   "Minh/data/images/teleport/door4.png"],
                                    loop=True)

    def render(self, canvas, x, y):
        self.gate_ani.render(canvas, x, y)

    def update(self, direction):
        pass
