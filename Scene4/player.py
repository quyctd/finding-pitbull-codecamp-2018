import pygame

from Scene4.box_collider import BoxCollider
from Scene4.game_object4_1 import GameObject
from Scene4.game_object4_1 import game_objects
from Scene4 import game_object4_1
from Scene4.frame_counter import FrameCounter
from Scene4.Part1.map_titles.platform import Platform
from Scene4.Part1.map_titles.grass import Grass
from Scene4.Part1.map_titles.hidden_grass import Hidden_Grass
from Scene4.Part1.map_titles.active_grass import Active_Grass
from Scene4.Part1.map_titles.locked_door import LockedDoor
from Scene4.player_anim.player_animation import PlayerAnimation
from Scene4.player_anim.player_death import PlayerDeath

class Player(GameObject):
    def __init__(self, x, y,  input_manager):
        GameObject.__init__(self, x,  y)
        self.image = pygame.image.load('Scene4/images/player/player_stand.png')
        self.image = pygame.transform.scale(self.image, (32, 64))
        self.width = self.image.get_width()
        self.heigth = self.image.get_height()
        self.win = False
        self.isJump = False
        self.speed = 4
        self.jumpHight = 16
        self.input_manager = input_manager
        self.counter = FrameCounter(24)
        self.pressJump = False
        self.collider = BoxCollider(self.width, self.heigth)
        self.resetLock()
        self.Alive = True
        self.renderer = PlayerAnimation()
        self.dx = 0
        self.dy = 0

    def resetLock(self):
        self.lockDown = False
        self.lockUp = False
        self.lockLeft = False
        self.lockRight = False

    def update(self):

        if not self.Alive:
            return None
        self.update_animator()

        # print(self.y)
        self.collider.x = self.x
        self.collider.y = self.y
        self.resetLock()
        self.collide()

        # gavity

        if self.isJump == False:
            if not self.lockDown:
                self.y += self.jumpHight
                # print(self.jumpHight)
            else:
                # self.dy = 0
                self.counter.count = self.counter.count_max
                if self.jumpHight > 32 :
                    self.jumpHight = 32
            # print(self.limitDown, self.y)

        self.move()
        if self.y > 680 :
            self.Alive = False
    def update_animator(self):
        self.renderer.update(self.dx, self.dy)

    def collide(self):
        left, right, top, bot = self.collider.corners()
        # print(left, right, top, bot)

        collide_at_peak = []

        for game_object in game_objects:
            # print(game_object.x , game_object.y)
            if game_object.collider is not None and self.collider.overlap(game_object.collider) :#and game_object.image is not None:
                if type(game_object) == Platform or type(game_object) == Grass or type(game_object) == Hidden_Grass or (type(game_object) == Active_Grass and game_object.isActive):
                    gleft, gright, gtop, gbot = game_object.collider.corners()
                    if type(game_object) == Hidden_Grass:
                        game_object.isActive = True
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
                elif type(game_object) == LockedDoor:
                    self.win = True
                elif type(game_object) is not Active_Grass:
                    game_object.isActive = True
                    self.Alive = False
                    self.image = None
                    death = PlayerDeath(self.x, self.y)
                    game_object4_1.add(death)



        if not self.lockDown:
            for game_object in collide_at_peak:
                gleft, gright, gtop, gbot = game_object.collider.corners()
                if left == gright:
                    self.lockLeft = True
                if right == gleft:
                    self.lockRight = True

    def move(self):

        self.dx =  0
        self.dy = 0

        # move left
        if self.input_manager.left_pressed and not self.lockLeft:
            self.dx = -1
            if game_object4_1.start_point.x == 0 or self.x > 672:
                self.x -= self.speed
            else:
                for game_object in game_objects:
                    if type(game_object) is not "Player":
                        game_object.x += self.speed
                game_object4_1.start_point.x += self.speed
                game_object4_1.finish_point.x += self.speed

        # move right
        if self.input_manager.right_pressed and not self.lockRight:
            self.dx = 1
            if game_object4_1.finish_point.x == 800+16 or self.x < 128:
                self.x += self.speed
            else:
                for game_object in game_objects:
                    if type(game_object) is not "Player":
                        game_object.x -= self.speed
                game_object4_1.start_point.x -= self.speed
                game_object4_1.finish_point.x -= self.speed

        # jump
        if self.input_manager.up_pressed and not self.pressJump and self.lockDown:
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




