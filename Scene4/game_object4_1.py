import pygame

game_objects = []

def add(game_objetct):
    game_objects.append(game_objetct)

def render(canvas):
    for game_object in game_objects:
        if game_object.isActive:
            game_object.render(canvas)

def update():
    for game_object in game_objects :
        # if game_object.isActive == True:
        game_object.update()

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isActive = True
        self.image = None
        self.collider = None
        self.renderer = None

    def render(self, canvas):
        if self.renderer is not None:
            self.renderer.render(canvas, self.x, self.y)
        if self.image is not None:
            width = self.image.get_width()
            height = self.image.get_height()
            render_pos = (self.x - width / 2, self.y - height / 2)
            canvas.blit(self.image, render_pos)
        # if self.collider is not None:
        #     self.collider.render(canvas)

    def update(self):
        if self.collider is not None:
            self.collider.x = self.x
            self.collider.y = self.y

    def collide_with(self, typeObj):
        collide_list = []
        for game_object in game_objects:
            if type(game_object) == typeObj and self.collider.overlap(game_object) :
                collide_list.append(game_object)
        return collide_list

start_point = GameObject(0 ,0)
finish_point = GameObject(3056, 0)
