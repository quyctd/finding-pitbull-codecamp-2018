import pygame
from Minh import game_object
from Minh.player import player
from Minh.physics.box_collider import BoxCollider


class CollapseObject:

    def __init__(self, x, y, display, x_activate, y_activate, player, gravity):
        self.x = x
        self.y = y
        self.image = pygame.image.load("Minh/data/images/wall.png")
        self.display = display
        self.box_collider = None
        self.collider_activate = True
        self.x_activate = x_activate
        self.y_activate = y_activate
        self.player = player
        self.gravity = gravity

    def update(self):
        collide_list = game_object.collide_with(self.box_collider)
        for obj in collide_list:
            if type(obj) == player.Player:
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

    def render(self, canvas):
        if self.image is not None:
            canvas.blit(self.image, (self.x, self.y))
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)
        if self.collider_activate:
            if self.display:
                self.box_collider = BoxCollider(32, 42, self)

    def impact(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x + self.image.get_width() / 2
            self.box_collider.y = self.y + self.image.get_height() / 2

    def activate(self):
        if self.collider_activate:
            if -21 <= ((self.player.x + self.player.img_right.get_width() / 2) - self.x_activate) <= 21 and \
                    -21 <= ((self.player.y + self.player.img_right.get_height() / 2) - self.y_activate) <= 21:
                if self.display:
                    self.display = False
                    self.box_collider = None
                else:
                    self.display = True
                    self.box_collider = BoxCollider(25, 42, self)
                self.collider_activate = False
