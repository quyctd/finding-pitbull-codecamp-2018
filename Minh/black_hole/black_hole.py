from Minh.gate.gate import Gate
from Minh.physics.box_collider import BoxCollider
from Minh.player.black_hole_animation import BlackHoleAnimation


class BlackHole(Gate):

    def __init__(self, x, y, detination, image, teleport, player, gravity):
        Gate.__init__(self, x, y, detination, image, teleport, player, gravity)
        self.box_collider = BoxCollider(126, 126, self)
        self.animation = BlackHoleAnimation()

    def render(self, canvas):
        self.animation.render(canvas, self.x, self.y)
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)
