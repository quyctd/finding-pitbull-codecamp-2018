game_objects = []


def add(game_object):
    game_objects.append(game_object)


def update():
    for game_object in game_objects:
        if game_object.is_active:
            game_object.update()


def render(canvas):
    for game_object in game_objects:
        if game_object.is_active:
            game_object.render(canvas)


def collide_with(box_collider, wanted_type):
    collide_list = []
    for game_object in game_objects:
        if game_object.is_active and game_object.box_collider is not None:
            if type(game_object) == wanted_type:
                if game_object.box_collider.overlap(box_collider):
                    collide_list.append(game_object)

    return collide_list


class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.renderer = None
        self.is_active = True
        self.box_collider = None


    def update(self):
        if self.box_collider is not None:
            self.box_collider.x = self.x
            self.box_collider.y = self.y

    def render(self, canvas):
        if self.renderer is not None:
            self.renderer.render(canvas, self.x, self.y)


    def deactivate(self):
        self.is_active = False


start_point = GameObject(0, 0)
finish_point = GameObject(1616, 0)