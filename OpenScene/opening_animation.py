import pygame
from Minh.player.animation import Animation


class OpeningAnimation:

    def __init__(self):
        self.op_animation = Animation(["Scene1/to_elevator/comein2.png",
                                         "Scene1/to_elevator/comein1.png",
                                         "Scene1/to_elevator/comein3.png",
                                         "Scene1/to_elevator/comein4.png",
                                       "OpenScene/images/elevator/thangmay1.png",
                                       "OpenScene/images/elevator/thangmay2.png",
                                       "OpenScene/images/elevator/thangmay3.png",
                                       "OpenScene/images/elevator/thangmay4.png",
                                       "OpenScene/images/elevator/thangmay5.png",
                                       "OpenScene/images/elevator/thangmay6.png",
                                       "OpenScene/images/elevator/thangmay7.png",
                                       "OpenScene/images/elevator/thangmay8.png",
                                       "OpenScene/images/elevator/thangmay9.png"
                                       ],
                                        loop=False)

    def render(self, canvas, x, y):
        self.op_animation.render(canvas, x, y)

    def update(self):
        pass
