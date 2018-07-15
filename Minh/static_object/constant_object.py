import pygame
from Minh.game_object import GameObject
from Minh.physics.box_collider import BoxCollider
from Minh.game_object import collide_with
from Minh.player.player import Player


class ConstantObject(GameObject):

    def __init__(self, x, y, gravity):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load("Minh/data/images/wall.png")
        self.box_collider = BoxCollider(32, 42, self)
        self.gravity = gravity

    def update(self):
        collide_list = collide_with(self.box_collider)
        for obj in collide_list:
            if type(obj) == Player:
                left1, right1, top1, bot1 = self.box_collider.corners()
                left2, right2, top2, bot2 = obj.box_collider.corners()
                if right2 - left1 > bot1 - top2:
                    if right1 - left2 > bot1 - top2:
                        obj.y = int(bot1) + 4
                    elif right1 - left2 == bot1 - top2:
                        pass
                    else:
                        obj.x = int(right1)
                else:
                    if right1 - left2 > bot1 - top2:
                        obj.x = int(left1) - obj.box_collider.width
                    elif right1 - left2 == bot1 - top2:
                        pass
                    else:
                        obj.can_jump = True
                        self.gravity.is_activated = False
                        obj.y = int(top1) - obj.box_collider.height - 4
            break
