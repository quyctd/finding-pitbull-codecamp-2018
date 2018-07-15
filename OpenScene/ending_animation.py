import pygame
from Minh.player.animation import Animation


class EndingAnimation:

    def __init__(self):
        self.ed_animation = Animation([
                                       "OpenScene/images/elevator/thangmay9.png",
                                       "OpenScene/images/elevator/thangmay8.png",
                                        "EndScene/outtro.2.png",
            "EndScene/outtro.3.png","EndScene/outtro.4.png","EndScene/outtro.5.png","EndScene/outtro.6.png",
            "EndScene/outtro.7.png", "EndScene/outtro.8.png", "EndScene/outtro.9.png", "EndScene/outtro.10.png",
            "EndScene/outtro.11.png", "EndScene/outtro.12.png", "EndScene/outtro.13.png", "EndScene/outtro.14.png",
            "EndScene/outtro.15.png", "EndScene/GameOver.jpg"
                                       ],
                                        loop=False)

    def render(self, canvas, x, y):
        self.ed_animation.render(canvas, x, y)

    def update(self):
        pass
