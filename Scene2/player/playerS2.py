import pygame

from Scene2.physics.box_collider import BoxCollider
from Scene2.game_objectS2 import GameObject
from Scene2.game_objectS2 import game_objects
from Scene2 import game_objectS2
from Scene2.frame_counterS2 import FrameCounter
from Scene2.map_titles.platform import Platform
from Scene2.map_titles.spike import Spike
from Scene2.player.player_death import PlayerDeath
from Scene2.game_objectS2 import collide_with
from Scene2.player.player_animation import PlayerAnimation
from Scene2.map_titles.spikeDown import Spike1
from Scene2.map_titles.spikeLeft import Spike2
from Scene2.map_titles.spikeRight import Spike3
from Scene2.map_titles.grass import Grass
from Scene2.map_titles.hiddenSpike import HiddenSpike
from Scene2.map_titles.endDoor import EndDoor
from Scene2.renderer.image_renderer import ImageRenderer

class Player(GameObject):
    def __init__(self, x, y,  input_manager):
        GameObject.__init__(self, x,  y)
        self.image = pygame.image.load("Scene2/image/player/player1.png")
        self.image = pygame.transform.scale(self.image, (32, 64))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.isJump = False
        self.speed = 4
        self.jumpHight = 16
        self.input_manager = input_manager
        self.counter = FrameCounter(24)
        self.pressJump = False
        self.box_collider = BoxCollider(self.width, self.height)
        self.resetLock()
        self.Alive = True
        self.dx = 0
        self.dy = 0
        self.renderer = PlayerAnimation()
        self.win = False

    def resetLock(self):
        self.lockDown = False
        self.lockUp = False
        self.lockLeft = False
        self.lockRight = False

    def update(self):
        # print(self.y)
        if not self.Alive:
            return None
        self.update_animator()
        self.box_collider.x = self.x
        self.box_collider.y = self.y
        self.resetLock()
        self.collider()

        collide_list = collide_with(self.box_collider, Spike)
        for object in collide_list:
            self.deactivate()
            death = PlayerDeath(self.x, self.y)
            game_objectS2.add(death)

        collide_list = collide_with(self.box_collider, Spike1)
        for object in collide_list:
            self.deactivate()
            death = PlayerDeath(self.x, self.y)
            game_objectS2.add(death)

        collide_list = collide_with(self.box_collider, Spike2)
        for object in collide_list:
            self.deactivate()
            death = PlayerDeath(self.x, self.y)
            game_objectS2.add(death)

        collide_list = collide_with(self.box_collider, Spike3)
        for object in collide_list:
            self.deactivate()
            death = PlayerDeath(self.x, self.y)
            game_objectS2.add(death)

        collide_list = collide_with(self.box_collider, EndDoor)
        if len(collide_list) > 0:
            self.win = True
            return None

        collide_list = collide_with(self.box_collider, HiddenSpike)
        for object in collide_list:
            object.renderer = ImageRenderer("Scene2/assets/images/sprite/spike0001.png")
            death = PlayerDeath(self.x, self.y)
            game_objectS2.add(death)

        # gravity
        if self.isJump == False:
            if not self.lockDown:
                self.y += self.jumpHight
                # print(self.jumpHight)
            else:
                # self.dy = 0
                self.counter.count = self.counter.count_max
                if self.jumpHight > 32 :
                    self.jumpHight = 32
        self.move()
        if self.y > 680 :
            self.Alive = False

    def update_animator(self):
        self.renderer.update(self.dx, self.dy)


    def collider(self):
        left, right, top, bot = self.box_collider.corners()
        # print(left, right, top, bot)

        collide_at_peak = []

        for game_object in game_objects:
            # print(game_object.x , game_object.y)
            if game_object.box_collider is not None and self.box_collider.overlap(game_object.box_collider) :#and game_object.image is not None:
                if type(game_object) == Platform:
                    gleft, gright, gtop, gbot = game_object.box_collider.corners()
                    cnt = 0
                    if bot == gtop or top == gbot:
                        cnt += 1
                    if left == gright or right == gleft:
                        cnt += 1

                    if cnt == 2:
                        collide_at_peak.append(game_object)
                    else:
                        if bot == gtop:
                            self.lockDown = True
                        elif top == gbot:
                            # if game_object.image == None:
                            #     print(type(game_object) , gtop , gbot, gleft, gright)
                            self.lockUp = True
                        elif left == gright:
                            self.lockLeft = True
                        elif right == gleft:
                            self.lockRight = True
                elif type(game_object) == Grass:
                    game_object.isActive = False
                    game_object.deactivate()
                else:
                    game_object.isActive = True
                    self.deactivate()
                    self.Alive = False




        if not self.lockDown:
            for game_object in collide_at_peak:
                gleft, gright, gtop, gbot = game_object.box_collider.corners()
                if left == gright:
                    self.lockLeft = True
                if right == gleft:
                    self.lockRight = True

    def move(self):
        self.dx = 0
        self.dy = 0
        # move left
        if self.input_manager.left_pressed and not self.lockLeft:
            self.dx = -1

            if game_objectS2.start_point.x == 0 or self.x > 672:
                self.x -= self.speed
            else:
                for game_object in game_objects:
                    if type(game_object) is not "Player":
                        game_object.x += self.speed
                game_objectS2.start_point.x += self.speed
                game_objectS2.finish_point.x += self.speed

        # move right
        if self.input_manager.right_pressed and not self.lockRight:
            self.dx = 1

            if game_objectS2.finish_point.x == 800+16 or self.x < 128:
                self.x += self.speed

            else:
                for game_object in game_objects:
                    if type(game_object) is not "Player":
                        game_object.x -= self.speed
                game_objectS2.start_point.x -= self.speed
                game_objectS2.finish_point.x -= self.speed

        # jump
        if self.input_manager.up_pressed and not self.pressJump and self.lockDown:
            self.dy = -1
            self.pressJump = True
            self.isJump = True
            self.counter.reset()
            self.jumpHight = 32

        if self.pressJump:
            self.dy = 1
            if self.counter.count < self.counter.count_max // 2:
                if self.counter.count % 4 == 0:
                    self.jumpHight /= 2

                # print(self.counter.count , self.lockUp)
                if not self.lockUp:
                    self.y -= self.jumpHight
                    # print(self.jumpHight)
                    # print(2 , self.y, self.counter.count_max , self.counter.count)
                else:
                    self.counter.count = self.counter.count_max - self.counter.count - 1
                    # self.jumpHight *= 2
            else:
                # if self.counter.count == self.counter.count_max // 2:
                #     self.jumpHight /= 2
                if self.counter.count % 4 == 0 and not self.counter.expired and self.counter.count is not self.counter.count_max // 2:
                    self.jumpHight *= 2
                # print(self.jumpHight)
                self.isJump = False
            self.counter.run()

        if self.counter.expired:
            self.counter.reset()
            self.pressJump = False
        # print(self.dx)





