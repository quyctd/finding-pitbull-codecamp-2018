class Gravity:

    def __init__(self, player):
        self.player = player
        self.is_activated = True

    def impact(self):
        if self.is_activated:
            self.player.y += 1
