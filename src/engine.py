import os
import random
import time
from map import Map
from map_file_reader import MapFileReader
from map_renderer import MapRenderer


class Engine:
    def __init__(self, tick_interval_in_seconds):
        self.tick_interval_in_seconds = tick_interval_in_seconds

        print("Looking for maps.")
        folder = os.path.join(os.path.dirname(__file__), "..", "maps")
        folder = os.path.abspath(folder)  # optional, resolves to absolute path
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        file = random.choice(files)
        print("Found map file '{}'".format(file))
        lines: list[str]
        with open(os.path.join(folder, file), "r") as f:
            lines = list(f)
        max_width = 80
        max_height = 30
        map_reader = MapFileReader(lines, max_width, max_height)
        description = map_reader.create_map_definition()
        self.map = Map(description, max_width, max_height)

    def start(self):
        while True:
            MapRenderer.render_map(self.map)
            time.sleep(self.tick_interval_in_seconds)
