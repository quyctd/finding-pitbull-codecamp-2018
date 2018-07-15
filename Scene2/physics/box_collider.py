from Scene2.game_objectS2 import GameObject
import pygame


class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self, 0, 0)
        self.width = width
        self.height = height

    def render(self, canvas):
        RED = (255, 0, 0)
        rect = (self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(canvas, RED, rect, 1)

    def corners(self):
        return(self.x - self.width / 2,
               self.x + self.width / 2,
               self.y - self.height / 2,
               self.y + self.height / 2
        )

    def overlap(self, other):
        left1, right1, top1, bot1 = self.corners()
        left2, right2, top2, bot2 = other.corners()
        if left1 <= right2 and right1 >= left2 and top1 <= bot2 and bot1 >= top2:
            return True
        else:
            return False