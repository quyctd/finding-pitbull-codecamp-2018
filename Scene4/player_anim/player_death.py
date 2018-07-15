from Scene4.game_object4_1 import GameObject
from Scene4.renderer.animation import Animation
from Scene4.frame_counter import FrameCounter




class PlayerDeath(GameObject):
    def __init__(self, x, y, frame_delay=1):
        self.frame_counter = FrameCounter(frame_delay)
        GameObject.__init__(self, x, y)
        self.renderer = Animation(["Scene4/images/player/player_stand.png",
                                   "Scene4/images/player/playerDeath1.png",
                                   "Scene4/images/player/playerDeath2.png",
                                   "Scene4/images/player/playerDeath3.png"])
