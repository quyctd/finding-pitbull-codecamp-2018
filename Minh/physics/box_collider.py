import pygame


class BoxCollider:

    def __init__(self, width, height, obj):
        try:
            self.x = obj.x + obj.image.get_width() / 2
            self.y = obj.y + obj.image.get_height() / 2
        except AttributeError:
            self.x = obj.x
            self.y = obj.y
        self.width = width
        self.height = height

    def render(self, canvas):
        rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        # pygame.draw.rect(canvas, (0, 255, 0), rect, 1)

    def corners(self):
        return (
            self.x - self.width / 2,
            self.x + self.width / 2,
            self.y - self.height / 2,
            self.y + self.height / 2
        )

    def overlap(self, other):
        left1, right1, top1, bot1 = self.corners()
        left2, right2, top2, bot2 = other.corners()
        if left1 < right2 and right1 > left2 and top1 - 4 < bot2 and bot1 + 4 > top2:
            return True
        else:
            return False
