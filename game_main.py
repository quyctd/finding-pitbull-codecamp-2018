import pygame
from Scene4.Part1 import manager1
from Scene2 import TrollGame_codeS2
from Scene1.Phantich import Scene1
from OpenScene import opmanager
from OpenScene.edmanager import Main
from Minh import main

pygame.init()
loop = 1
SIZE = (800, 640)
canvas = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Finding Pug")

scene_1 = Scene1()
opening = opmanager.Main(scene_1)
ending = Main()
scene_2 = TrollGame_codeS2.Main()
scene_3 = main.Main()
scene_4 = manager1.Main()

list_scene = [opening, scene_2, scene_3, scene_4, ending]

gameplay = True


def change_scene(scene):
    game = scene
    return game

# a = scene_4.update(canvas)
# print(a)
for scene in list_scene:

    game = change_scene(scene)
    game.update(canvas)
    if game.pressClose:
        break
# ending.update(canvas)
