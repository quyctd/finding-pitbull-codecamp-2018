import json
from addict import Dict
from Scene2.map_titles.platform import Platform
from Scene2.map_titles.grass import Grass
from Scene2.map_titles.spike import Spike
from Scene2.map_titles.jet import Jet
from Scene2.map_titles.spikeDown import Spike1
from Scene2.map_titles.spikeLeft import Spike2
from Scene2.map_titles.spikeRight import Spike3
from Scene2.map_titles.hiddenSpike import HiddenSpike
from Scene2.map_titles.endDoor import EndDoor
import Scene2.game_objectS2


def load_map(json_file_url):
    #  1. Load json file => text
    text = open(json_file_url, "r").read()
    # print(text)

    # 2. Convert text into dictionary
    map_dict = json.loads(text)

    # 3. Convert dictionary to object
    map = Dict(map_dict)

    data = map_dict["layers"][0]["data"]  # list
    width = map_dict["width"]
    height = map_dict["height"]

    return data, width, height


def generate_map(json_file_url):  # assets/maps/tut_lvl.json
    data, width, height = load_map(json_file_url)

    for index, title in enumerate(data):
        title_x = index % width
        title_y = index // width
        if title == 0:
            pass
        elif title == 1:
            Scene2.game_objectS2.add(Platform(title_x * 32 + 16, title_y * 32 + 16))
        elif title == 2:
            Scene2.game_objectS2.add((Jet(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 3:
            Scene2.game_objectS2.add((Spike1(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 4:
            Scene2.game_objectS2.add((Spike2(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 5:
            Scene2.game_objectS2.add((Spike3(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 6:
            Scene2.game_objectS2.add((Spike(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 7:
            Scene2.game_objectS2.add((Grass(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 8:
            Scene2.game_objectS2.add((HiddenSpike(title_x * 32 + 16, title_y * 32 + 16)))
        elif title == 9:
            Scene2.game_objectS2.add((EndDoor(title_x * 32 + 16, title_y * 32 + 16)))


if __name__ == "__main__":
    generate_map("Scene2/assets/maps/tut_lvl.json")
