from Scene2.game_objectS2 import GameObject
from Scene2.renderer.animation import Animation
from Scene2.frame_counterS2 import FrameCounter




class PlayerDeath(GameObject):
    def __init__(self, x, y, frame_delay=1):
        self.frame_counter = FrameCounter(frame_delay)
        GameObject.__init__(self, x, y)
        self.renderer = Animation(["image/player/player1.png",
                                   "image/player/playerDeath1.png",
                                   "image/player/playerDeath2.png",
                                   "image/player/playerDeath3.png"])
