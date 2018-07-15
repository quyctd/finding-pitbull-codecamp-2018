import pygame
from pygame.locals import *
from Scene4.input_manager import InputManager
from Scene4.player import Player
from Scene4 import game_object4_1
from Scene4.Part1 import map_generator
# from elevator import Elevator
from Scene4.game_object4_1 import GameObject
from Scene4.frame_counter import FrameCounter
# from Scene4.box_collider import BoxCollider

class Main():
    def __init__(self):
        # Init pygame
        self.end = False
        # self.elevator = Elevator(2 * 32, 13 * 32, BoxCollider(64, 64), None)
        self.pressClose = False


    def update(self, canvas):
        ffont = pygame.font.Font(None, 100)
        # import BackGround
        frame_counter = FrameCounter(40)

        # Clock
        clock = pygame.time.Clock()
        map_generator.generate_map("Scene4/Part1/map/map4.json")
        input_manager = InputManager()
        player = Player(124 , 416, input_manager)
        # self.elevator.player = player
        loop = True
        pressReset = False
        shut_down = False
        pygame.mixer.music.load('Scene4/sound/Scene4.mp3')
        pygame.mixer.music.play(-1)

        CorrectPass = "1612"
        PlayerPass = ""
        dead = pygame.mixer.Sound('Scene4/sound/dead.mp3')

        played_sound = False


        while loop:
            # if self.elevator.pressClose:
            #     loop = False
            #     shut_down = True
            #     self.pressClose = True
            #
            if pressReset:
                cnt = 0
                # pygame.mixer.music.load('Scene4/sound/Scene4.mp3')
                pygame.mixer.music.play(-1)
                while len(game_object4_1.game_objects) > 0:
                    for game_object in game_object4_1.game_objects:
                        # print(game_object.x)
                        game_object4_1.game_objects.remove(game_object)
                map_generator.generate_map("Scene4/Part1/map/map4.json")
                player = Player(124, 416, input_manager)
                game_object4_1.start_point = GameObject(0, 0)
                game_object4_1.finish_point = GameObject(3056, 0)
                pressReset = False
                played_sound = False
        # ---------------------------------------------------------------------------------------------------------
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop = False
                    shut_down = True
                    self.pressClose = True
                else:
                    input_manager.update(even)
        # -------------------------------------------------------------------------------------------------------
            canvas.blit(pygame.image.load('Scene4/images/BackGround4.jpg'), (0, 0))
            player.update()
            game_object4_1.update()
            game_object4_1.render(canvas)

            # draw

            if player.Alive:
                player.renderer.render(canvas, player.x, player.y)
            # canvas.blit(player.image, (player.x - player.width//2, player.y - player.heigth//2))

            # canvas.fill((100 , 150, 200))

        # ------------------------------------------------------------------------------------------------------------------
            if player.win:
                loop = False
        # ------------------------------------------------------------------------------------------------------------------
            if not player.Alive:
                pygame.mixer.music.stop()
                if not played_sound:
                    dead.play()
                    played_sound = True
                frame_counter.run()
            if frame_counter.expired :
                frame_counter.reset()
                pressReset = True
            pygame.display.flip()
            clock.tick(60)


        canvas.blit(pygame.image.load('Scene4/images/PasswordScene.png') , (0, 0))
        if not shut_down:
            loop = True
        while loop:
            events = pygame.event.get()
            for even in events:
                if (even.type == pygame.QUIT) or (even.type == KEYDOWN and even.key == K_ESCAPE):
                    loop = False
                    self.pressClose = True
                elif even.type == KEYDOWN:
                    if even.key == pygame.K_RETURN:
                        if PlayerPass == CorrectPass:
                            loop = False
                            self.end = True
                        else:
                            PlayerPass = ""
                            canvas.blit(pygame.image.load('Scene4/images/PasswordScene.png'), (0, 0))
                    elif even.key is not pygame.K_BACKSPACE:
                        PlayerPass += even.unicode
                    else:
                        PlayerPass = PlayerPass[:-1]
                        canvas.blit(pygame.image.load('Scene4/images/PasswordScene.png'), (0, 0))
                chu = ffont.render(PlayerPass, True, (255, 0, 0))
                canvas.blit(chu, (300, 300))
            pygame.display.flip()
            clock.tick(60)
        self.end = True
