import pygame
from pygame.locals import *
from Scene2 import game_objectS2
from Scene2.input.input_managerS2 import InputManager
from Scene2.player.playerS2 import Player
from Scene2.map.map_generator import generate_map
from Scene2.game_objectS2 import GameObject
from Scene2.frame_counterS2 import FrameCounter
from Scene2.input.input_managerS2 import global_input_manager

class Main():
    def __init__(self):

        self.end = False
        self.pressClose = False

    def update(self, canvas):
        # set screen
        BG = (50, 50, 50)

        # Clock
        clock = pygame.time.Clock()

        input_manager = InputManager()

        player = Player(132, 160, global_input_manager)
        generate_map("Scene2/assets/maps/tut_lvl.json")
        frame_delay = FrameCounter(60)

        dead = pygame.mixer.Sound('Scene4/sound/dead.mp3')
        pygame.mixer.music.load('Scene2/sound/brackground2.mp3')
        pygame.mixer.music.play(-1)

        loop = True
        pressReset = False
        played_music = False

        while loop:
            if pressReset:
                pygame.mixer.music.play(-1)
                cnt = 0
                while len(game_objectS2.game_objects) > 0:
                    for game_object in game_objectS2.game_objects :
                        # print(game_object.x)
                        game_objectS2.game_objects.remove(game_object)
                generate_map("Scene2/assets/maps/tut_lvl.json")
                player = Player(124, 416, global_input_manager)
                game_objectS2.start_point = GameObject(0, 0)
                game_objectS2.finish_point = GameObject(1616, 0)
                pressReset = False
                played_music = False
            # Event processing
            events = pygame.event.get()
            for event in events:
                if (event.type == pygame.QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    loop = False
                    self.pressClose = True
                else:
                    global_input_manager.update(event)

            canvas.fill(BG)
            player.update()

            if player.win:
                loop = False

            canvas.blit(pygame.image.load('Scene4/images/BackGround4.jpg'), (0, 0))
            # canvas.blit(player.image, (player.x - player.width // 2, player.y - player.height // 2))
            if player.Alive:
                player.renderer.render(canvas, player.x, player.y)
            # player.box_collider.render(canvas)
            game_objectS2.update()
            game_objectS2.render(canvas)
            # print(player.Alive)
            pygame.display.flip()
            if not player.Alive:
                if not played_music:
                    pygame.mixer.music.stop()
                    dead.play()
                    played_music = True
                frame_delay.run()
            if frame_delay.expired:
                frame_delay.reset()
                pressReset = True
            clock.tick(60)
        pygame.mixer.music.stop()
        self.end = True