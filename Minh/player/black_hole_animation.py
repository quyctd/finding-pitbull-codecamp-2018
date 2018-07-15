import pygame
from Minh.player.animation import Animation


class BlackHoleAnimation:

    def __init__(self):
        self.bh_animation = Animation(["Minh/data/images/blackhole/bh1.png",
                                         "Minh/data/images/blackhole/bh2.png",
                                         "Minh/data/images/blackhole/bh3.png",
                                         "Minh/data/images/blackhole/bh4.png",
                                         "Minh/data/images/blackhole/bh5.png",
                                         "Minh/data/images/blackhole/bh6.png",
                                         "Minh/data/images/blackhole/bh7.png"],
                                        loop=True)

    def render(self, canvas, x, y):
        self.bh_animation.render(canvas, x, y)

    def update(self, direction):
        pass

