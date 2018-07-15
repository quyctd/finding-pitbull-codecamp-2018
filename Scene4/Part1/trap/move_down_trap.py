from Scene4.trap_manager import Trap
from Scene4.box_collider import BoxCollider

class MoveDownTrap(Trap):
    def __init__(self, x, y, image_url, limity):
        Trap.__init__(self, x, y, image_url, limity)
        self.active_collider = BoxCollider()

    def update(self):
        if self.y < self.limity:
            self.y += self.spped
            if self.ground_collider is not None:
                self.ground_collider.y += self.speed




