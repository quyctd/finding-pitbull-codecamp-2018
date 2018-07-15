import pygame
import sys
from Minh.player.player import Player
from Minh import game_object
from Minh.data.map.map_generate import generate_map
from Minh.dynamic_wall.dynamic_wall import activate
from Minh.physics.gravity import Gravity
from pygame.locals import *



clock = pygame.time.Clock()

class Main():
    def __init__(self):

        self.end = False
        self.pressClose = False

    def update(self,canvas):
        dead = pygame.mixer.Sound('Scene4/sound/dead.mp3')
        pygame.mixer.music.load('Minh/sound/theme.mp3')

        scene_3 = True
        while scene_3:
            player = Player(84, 1176, None)
            game_object.add(player)
            gravity = Gravity(player)
            background = generate_map("Minh/data/map/lvl_3j.json", gravity, player)
            static_background = pygame.image.load("Minh/data/images/background.jpg")
            player.background = background
            pygame.mixer.music.play(-1)

            play = True
            a_press = False
            d_press = False
            played_music = False

            while play:
                canvas.fill((50, 50, 50))
                if player.win:
                    play = False
                    scene_3 = False
                    self.end = True
                    pygame.mixer.music.stop()
                if player.die:
                    pygame.mixer.music.stop()
                    player.image = "death"
                    now = pygame.time.get_ticks()
                    if not played_music:
                        dead.play()
                        played_music = True
                    if player.death_time == 0:
                        player.death_time = now
                    else:
                        if now - player.death_time >= 1200:
                            play = False
                            object_list = game_object.game_objects.copy()
                            for obj in object_list:
                                game_object.game_objects.remove(obj)
                            dynamic_list = game_object.dynamic_objects.copy()
                            for dynamic_obj in dynamic_list:
                                game_object.dynamic_objects.remove(dynamic_obj)
                canvas.blit(static_background, (0, 0))
                now = pygame.time.get_ticks()
                if (now - player.jump_time) >= 400:
                    player.dir_y = 1
                    player.jump_time = 0

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        play = False
                        scene_3 = False
                        self.pressClose = True
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            a_press = True
                        elif event.key == K_RIGHT:
                            d_press = True
                        elif event.key == K_UP and player.can_jump:
                            player.image = "jump"
                            player.dir_y = -1
                            now = pygame.time.get_ticks()
                            player.jump_time = now
                        elif event.key == K_DOWN:
                            player.dir_y = 1
                    if event.type == KEYUP:
                        if event.key == K_LEFT:
                            a_press = False
                        elif event.key == K_RIGHT:
                            d_press = False
                    if a_press:
                        player.dir_x = -1
                        player.image = "left"
                    elif d_press:
                        player.dir_x = 1
                        player.image = "right"
                    else:
                        player.dir_x = 0
                if a_press or d_press or player.jump_time != 0 or player.die:
                    player.animation_active = True
                else:
                    player.animation_active = False
                player.can_jump = False
                gravity.is_activated = True
                player.update()
                player.activate()
                activate()
                player.update()
                game_object.change_scene(player, background, 800, 640, 1680, 1470)
                gravity.impact()
                game_object.render(canvas)
                player.render(canvas)
                pygame.display.update()
                clock.tick(60)