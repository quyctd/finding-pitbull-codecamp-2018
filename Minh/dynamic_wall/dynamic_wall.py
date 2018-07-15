import pygame
from Minh import game_object
from Minh.static_object.collapse_object import CollapseObject
from Minh.player import player
from Minh.physics.box_collider import BoxCollider


class DynamicWall:

    def __init__(self, x, y, kill, x_activate, y_activate, player, x_step, y_step, x_stop, y_stop, image,
                 box_collider_x, box_collider_y, again, gravity):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.is_activated = False
        self.allow_activate = True
        self.display = True
        self.box_collider = BoxCollider(box_collider_x, box_collider_y, self)
        self.kill = kill
        self.x_activate = x_activate
        self.y_activate = y_activate
        self.player = player
        self.x_step = x_step
        self.y_step = y_step
        self.x_stop = x_stop
        self.y_stop = y_stop
        self.again = again
        self.first_y = self.y
        self.gravity = gravity

    def update(self):
        collide_list = game_object.collide_with(self.box_collider)
        for obj in collide_list:
            if type(obj) == player.Player:
                if self.kill:
                    obj.die = True
                else:
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
                            if self.again:
                                for dynamic_obj in game_object.dynamic_objects:
                                    dynamic_obj.y -= 1
                                # self.y -= 1
                                if int(self.y) == int(self.first_y) - 42:
                                    for dynamic_obj in game_object.dynamic_objects:
                                        dynamic_obj.again = False
                                    # self.again = False
            break

    def activate(self):
        if self.allow_activate:
            if -21 <= ((self.player.x + self.player.img_right.get_width() / 2) - self.x_activate) <= 21 and\
                    -21 <= ((self.player.y + self.player.img_right.get_height() / 2) - self.y_activate) <= 21:
                self.is_activated = True
                self.allow_activate = False
        if self.is_activated:
            self.x += self.x_step
            self.y += self.y_step
            if self.x == self.x_stop and self.y == self.y_stop:
                self.is_activated = False

    def render(self, canvas):
        if self.image is not None:
            canvas.blit(self.image, (self.x, self.y))
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)

    def impact(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x + self.image.get_width() / 2
            self.box_collider.y = self.y + self.image.get_height() / 2


def activate():
    for obj in game_object.game_objects:
        if (type(obj) == DynamicWall) or (type(obj) == CollapseObject):
            obj.activate()
