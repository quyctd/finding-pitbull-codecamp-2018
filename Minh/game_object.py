from Minh.dynamic_wall.dynamic_wall import DynamicWall
from Minh.static_object.collapse_object import CollapseObject


game_objects = []
dynamic_objects = []


class GameObject:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.display = True
        self.box_collider = None

    def render(self, canvas):
        if self.image is not None:
            canvas.blit(self.image, (self.x, self.y))
        if self.box_collider is not None:
            self.impact()
            self.box_collider.render(canvas)

    def update(self):
        pass

    def activate(self):
        pass

    def impact(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x + self.image.get_width() / 2
            self.box_collider.y = self.y + self.image.get_height() / 2


def add(obj):
    game_objects.append(obj)


def dynamic_add(obj):
    dynamic_objects.append(obj)


def render(canvas):
    for obj in game_objects:
        if obj.display is not None:
            if obj.display:
                obj.render(canvas)


def change_scene(player, background, width, height, map_width, map_height):
    fixed_x = player.x
    fixed_y = player.y
    for obj in game_objects:
        obj.x -= fixed_x - width / 2
        obj.y -= fixed_y - height / 2
        if type(obj) == CollapseObject:
            obj.x_activate -= fixed_x - width / 2
            obj.y_activate -= fixed_y - height / 2
        if type(obj) == DynamicWall:
            obj.x_activate -= fixed_x - width / 2
            obj.y_activate -= fixed_y - height / 2
            obj.x_stop -= fixed_x - width / 2
            obj.y_stop -= fixed_y - height / 2
            obj.first_y -= fixed_y - height / 2

    bg_x = background.x
    bg_y = background.y
    bg_fixed_x = background.x
    bg_fixed_y = background.y
    if background.x <= width - map_width:
        bg_x = width - map_width
    if background.x >= 0:
        bg_x = 0
    if background.y >= 0:
        bg_y = 0
    if background.y <= height - map_height:
        bg_y = height - map_height
    for obj in game_objects:
        obj.x -= bg_fixed_x - bg_x
        obj.y -= bg_fixed_y - bg_y
        if type(obj) == CollapseObject:
            obj.x_activate -= bg_fixed_x - bg_x
            obj.y_activate -= bg_fixed_y - bg_y
        if type(obj) == DynamicWall:
            obj.x_activate -= bg_fixed_x - bg_x
            obj.y_activate -= bg_fixed_y - bg_y
            obj.x_stop -= bg_fixed_x - bg_x
            obj.y_stop -= bg_fixed_y - bg_y
            obj.first_y -= bg_fixed_y - bg_y


def collide_with(box_collide):
    collide_list = []
    for obj in game_objects:
        if obj.box_collider is not None and box_collide is not None:
            if obj.box_collider.overlap(box_collide):
                collide_list.append(obj)
    return collide_list
