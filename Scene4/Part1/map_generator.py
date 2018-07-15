from Scene4 import game_object4_1
import json
from addict import Dict
from Scene4.Part1.map_titles.platform import Platform
from Scene4.Part1.map_titles.grass import Grass
from Scene4.Part1.map_titles.hidden_thorn import Hidden_Thorn
from Scene4.Part1.map_titles.thorn import Thorn
from Scene4.Part1.map_titles.hight_thorn import Hight_Thorn
from Scene4.Part1.map_titles.left_thorn import Left_Thorn
from Scene4.Part1.map_titles.hidden_grass import Hidden_Grass
from Scene4.Part1.map_titles.laser import Laser
from Scene4.Part1.map_titles.locked_door import LockedDoor
from Scene4.Part1.map_titles.single_thorn import SingleThorn
from Scene4.Part1.map_titles.single_thorn_2 import SingleThorn_2
from Scene4.Part1.map_titles.single_thorn_3 import SingleThorn_3
from Scene4.Part1.map_titles.active_grass import Active_Grass

def load_map(json_file_url):
    text = open(json_file_url, "r").read()

    map_dict = json.loads(text)
    map = Dict(map_dict)

    data = map_dict["layers"][0]["data"]
    width = map.width
    height = map.height

    return (data, width, height)

def generate_map(json_file_url):
    data, width, height = load_map(json_file_url)

    for index, title in enumerate(data):
        x = index % width
        y = index // width

        if title == 2:
            game_object4_1.add(Platform(x * 32 + 16, y * 32 + 16))
        elif title == 6:
            game_object4_1.add(Hight_Thorn(x * 32 + 16, y * 32 + 16))
        elif title == 4:
            game_object4_1.add(Left_Thorn(x * 32 + 48, y * 32 + 16))
            game_object4_1.add(Hidden_Grass(x * 32 + 48 , y * 32 + 16))
            game_object4_1.add(Hidden_Grass(x * 32 + 80, y * 32 + 16))
        elif title == 5:
            game_object4_1.add(Thorn(x * 32 + 16, y * 32 + 16))
        elif title == 1:
            game_object4_1.add(Grass(x * 32 + 16, y * 32 + 16))
        elif title == 3:
            game_object4_1.add(Hidden_Thorn(x * 32 + 16, y * 32 + 16))
            # print(x , y)
        elif title == 13:
            game_object4_1.add(Laser(x*32 + 16, y* 32 - 32*7))
        elif title == 14:
            game_object4_1.add(LockedDoor(x*32 + 16 , y*32 - 32*8 + 16))
        elif title == 10:
            game_object4_1.add(SingleThorn(x*32 + 16, y*32- 16))
            # print(x , y)
        elif title == 11:
            game_object4_1.add(SingleThorn_2(x*32 + 16, y*32 - 32))
        elif title == 12:
            game_object4_1.add(SingleThorn_3(x*32 + 16, y*32 - 48))
        elif title == 8:
            game_object4_1.add(Active_Grass(x * 32 + 16, y * 32 + 16))



if __name__ == "__main__" :
    generate_map("Scene4/Part1/map/map4.json")