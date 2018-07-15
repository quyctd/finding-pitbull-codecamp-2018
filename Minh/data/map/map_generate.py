from Minh.static_object.constant_object import ConstantObject
from Minh.static_object.background import Background
from Minh.static_object.one_side_object1 import OneSideObject1
from Minh.black_hole.black_hole import BlackHole
from Minh.dynamic_wall.dynamic_wall import DynamicWall
from Minh.static_object.collapse_object import CollapseObject
from Minh.chest.chest import Chest
from Minh.gate.gate import Gate
from Minh.spike.spike import Spike
import json
import Minh.game_object as game_obj


def load_map(json_file_url):
    text = open(json_file_url, "r").read()
    map_dict = json.loads(text)
    data = map_dict["layers"][0]["data"]
    width = map_dict["width"]
    height = map_dict["height"]
    return data, width, height


def generate_map(json_file_url, gravity, player):
    data, width, height = load_map(json_file_url)

    background = Background(0, 0)
    game_obj.add(background)

    chest = Chest(37 * 42, 29 * 42, "Minh/data/images/chest.png")
    game_obj.add(chest)

    game_obj.add(ConstantObject(28 * 42, 8 * 42, gravity))
    game_obj.add(CollapseObject(35 * 42, 3 * 42, True, 35 * 42, 2 * 42, player, gravity))
    game_obj.add(CollapseObject(7 * 42, 5 * 42, True, 8 * 42, 4 * 42, player, gravity))
    game_obj.add(DynamicWall(23 * 42, 30 * 42, False, 24 * 42, 29 * 42, player, 0, -1, 23 * 42, 27 * 42,
                             "Minh/data/images/wall.png", 42, 42, False, gravity))
    game_obj.add(DynamicWall(24 * 42, 30 * 42, False, 24 * 42, 29 * 42, player, 0, -1, 24 * 42, 27 * 42,
                             "Minh/data/images/wall.png", 42, 42, False, gravity))
    game_obj.add(CollapseObject(24 * 42, 27 * 42, True, 24 * 42, 29 * 42, player, gravity))
    game_obj.add(CollapseObject(37 * 42, 21 * 42, False, 39 * 42, 23 * 42, player, gravity))
    game_obj.add(CollapseObject(38 * 42, 21 * 42, False, 39 * 42, 23 * 42, player, gravity))
    game_obj.add(DynamicWall(38 * 42, 30 * 42, False, 38 * 42 + 25, 29 * 42, player, 0, -3, 38 * 42, 24 * 42,
                             "Minh/data/images/wall.png", 42, 42, False, gravity))
    game_obj.add(ConstantObject(33 * 42, 21 * 42, gravity))
    game_obj.add(ConstantObject(33 * 42, 20 * 42, gravity))
    game_obj.add(ConstantObject(33 * 42, 19 * 42, gravity))
    game_obj.add(ConstantObject(33 * 42, 18 * 42, gravity))
    game_obj.add(ConstantObject(33 * 42, 17 * 42, gravity))
    game_obj.add(ConstantObject(34 * 42, 17 * 42, gravity))
    # game_obj.add(ConstantObject(28 * 42, 13 * 42, gravity))
    # game_obj.add(ConstantObject(29 * 42, 13 * 42, gravity))

    # game_obj.add(CollapseObject(23 * 42, 29 * 42, False, 1050, 1092, player, gravity))

    for index, title in enumerate(data):
        title_x = index % width
        title_y = index // width
        if title == 0:
            pass
        elif title == 1:
            # if (title_x == 35 and title_y == 31) or (title_x == 35 and title_y == 32):
            #         # or (title_x == 32 and title_y == 30) or (title_x == 33 and title_y == 30) or \
            #         # (title_x == 34 and title_y == 30) or (title_x == 35 and title_y == 30):
            #     pass
            # else:
            if (title_x == 7 and title_y == 5) or (title_x == 23 and title_y == 30) or (title_x == 24 and title_y == 30)\
                    or (title_x == 24 and title_y == 27) or (title_x == 38 and title_y == 30):
                pass
            elif title_x == 33 and title_y == 33:
                game_obj.add(OneSideObject1(33 * 42, 33 * 42, gravity))
            elif title_x == 34 and title_y == 33:
                game_obj.add(OneSideObject1(34 * 42, 33 * 42, gravity))
            else:
                game_obj.add(ConstantObject(title_x * 42, title_y * 42, gravity))
        elif title == 2:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 10, "Minh/data/images/door1.png", False, player, gravity))
        elif title == 3:
            if title_x == 28 and title_y == 33:
                pass
            else:
                game_obj.add(Spike(title_x * 42, title_y * 42, "Minh/data/images/spike.png"))
        elif title == 4:
            game_obj.add(Spike(title_x * 42, title_y * 42, "Minh/data/images/spike-right.png"))
        elif title == 5:
            pass
        elif title == 6:
            pass
        elif title == 7:
            game_obj.add(DynamicWall(title_x * 42, title_y * 42 - 294, True, 1596, 1218, player, 1, 0, 1690, 1218,
                                     "Minh/data/images/laze.png", 28, 336, False, gravity))
        elif title == 8:
            spike_down = DynamicWall(title_x * 42, title_y * 42, True, 630, 1008, player, 0, 2, title_x * 42, 1008,
                                     "Minh/data/images/spike-down.png", 28, 32, False, gravity)
            game_obj.add(spike_down)
            game_obj.dynamic_add(spike_down)
        elif title == 9:
            game_obj.add(BlackHole(title_x * 42, title_y * 42 - 84, 4, "Minh/data/images/black_hole.png", True, player, gravity))
        elif title == 10:
            game_obj.add(BlackHole(title_x * 42 + 42, title_y * 42 - 80, 4, "Minh/data/images/black_hole.png", False, player, gravity))
        elif title == 11:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 210, 2, "Minh/data/images/door.png", False, player, gravity))
        elif title == 12:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 3, "Minh/data/images/door.png", True, player, gravity))
        elif title == 13:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 2, "Minh/data/images/door.png", True, player, gravity))
        elif title == 14:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 3, "Minh/data/images/door.png", False, player, gravity))
        elif title == 15:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 1, "Minh/data/images/door.png", True, player, gravity))
        elif title == 16:
            game_obj.add(Gate(title_x * 42, title_y * 42 - 42, 1, "Minh/data/images/door.png", False, player, gravity))
        elif title == 17:
            dynamic_w = DynamicWall(title_x * 42, title_y * 42, False, 630, 1008, player, 0, 2, title_x * 42, 966,
                                     "Minh/data/images/wall.png", 42, 42, True, gravity)
            game_obj.dynamic_add(dynamic_w)
            game_obj.add(dynamic_w)
        elif title == 18:
            game_obj.add(CollapseObject(title_x * 42, title_y * 42, False, 1050, 1092, player, gravity))
        elif title == 19:
            game_obj.add(CollapseObject(title_x * 42, title_y * 42, True, 1050, 1092, player, gravity))
    return background