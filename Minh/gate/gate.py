import pygame
from Minh.game_object import game_objects
from Minh.game_object import GameObject
from Minh.game_object import collide_with
from Minh.player.player import Player
from Minh.gate.gate_animation import GateAnimation
from Minh.physics.box_collider import BoxCollider


class Gate(GameObject):

    def __init__(self, x, y, detination, image, teleport, player, gravity):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load(image)
        self.destination = detination
        self.teleport = teleport
        self.box_collider = BoxCollider(42, 84, self)
        self.player = player
        self.gravity = gravity
        self.gate_animation = GateAnimation()

    def render(self, canvas):
        self.gate_animation.render(canvas, self.x, self.y)
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)

    def update(self):
        if self.destination == 10:
            self.player.win = True
        if self.teleport:
            collide_list = collide_with(self.box_collider)
            for obj in collide_list:
                if type(obj) == Player:
                    for part in game_objects:
                        if type(part) == type(self) and part != self and part.teleport is False \
                                and part.destination == self.destination:
                            obj.x = part.x
                            obj.y = part.y
                            break
                break
