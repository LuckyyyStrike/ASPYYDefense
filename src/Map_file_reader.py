import Map_Description
from constants import Entity_Symbols
from Map_Description import Map_Description


class Map_file_reader:
    def __init__(self, lines: list[str], max_width: int, max_height: int):
        self.lines = lines
        self.max_width = max_width
        self.max_height = max_height

        columns_out_of_bounds = filter(lambda line: len(line) > max_width, lines)
        if len(list(columns_out_of_bounds)) > 0:
            raise ValueError("File has too many columns. Max column size is {}.".format(max_width))

        if len(lines) > max_height:
            raise ValueError("File has too many rows. Max row size is {}.".format(max_height))

        joined_lines = "".join(lines)
        Map_file_reader._check_for_singleton_character(
            joined_lines, Entity_Symbols.entry_point, "entry"
        )
        Map_file_reader._check_for_singleton_character(
            joined_lines, Entity_Symbols.exit_point, "exit"
        )

    def create_map_definition(self):
        return Map_Description(self.max_width, self.max_height, self.lines)

    @staticmethod
    def _check_for_singleton_character(string: str, singleton: str, singleton_name: str):
        singleton_count = string.count(singleton)
        if singleton_count != 1:
            raise ValueError(
                "Map has {} {} points, but has to have exactly 1.".format(
                    singleton_count, singleton_name
                )
            )
