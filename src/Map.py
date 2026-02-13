from Map_file_reader import Map_file_reader
from constants import Literals
from Entity import Entity
from Map_Description import Map_Description


class Map:
    map_description: Map_Description
    max_width: int
    max_height: int

    _matrix: list[list[Entity]] = []

    def __init__(self, map_description: Map_Description, max_width: int, max_height: int):
        self.map_description = map_description
        self.max_width = max_width
        self.max_height = max_height

        # Initialize the matrix with the map description

        # First row contains a border and the title
        first_row = self.create_centered_row(Literals.border_title, 0, "=")
        self._matrix.append(first_row)

        # Beginning with the second row, we want to add some padding to center the map vertically
        row_index: int = 1
        padding_rows_count = max_height - len(map_description.lines)
        padding_rows_infront = padding_rows_count // 2
        padding_rows_after = padding_rows_infront + (padding_rows_count % 2)
        for row in range(padding_rows_infront - 1):
            padded_row = self.create_centered_row("", row_index, " ")
            self._matrix.append(padded_row)
            row_index += 1

        # This is a bit more complicated. To center the map horizontally we have to measure
        # the width of the longest line. Since all lines in a map-file are flush on the left
        # line we can calculate the padding in front universally for all lines
        longest_line = max(map_description.lines)
        # The -2 comes from the 2 characters we are using as a vertical border
        padding_infront = (self.max_width - 2 - len(longest_line)) // 2
        for map_line in map_description.lines:
            padding_behind = self.max_width - 2 - len(map_line) - padding_infront
            padded_row = self.create_row(map_line, row_index, " ", padding_infront, padding_behind)
            self._matrix.append(padded_row)
            row_index += 1

        # Then we add some padding lines to the end
        for row in range(padding_rows_after - 1):
            padded_row = self.create_centered_row("", row_index, " ")
            self._matrix.append(padded_row)
            row_index += 1

        # Finally we can end with another border
        last_row = self.create_centered_row("", row_index, "=")
        self._matrix.append(last_row)

    def create_centered_row(self, content: str, row_index: int, padding_character: str):
        columns_minus_content = self.max_width - len(content) - 2
        padding_infront = columns_minus_content // 2
        padding_after = padding_infront + (columns_minus_content % 2)
        return Map.create_row(content, row_index, padding_character, padding_infront, padding_after)

    @staticmethod
    def create_row(
        content: str,
        row_index: int,
        padding_character: str,
        padding_count_infront: int,
        padding_count_behind: int,
    ):
        columns: list[Entity] = [Entity(0, row_index, "I")]
        column_index = 1
        for column in range(padding_count_infront):
            columns.append(Entity(column_index, 0, padding_character))
            column_index += 1
        for content_character in content:
            columns.append(Entity(column_index, 0, content_character))
            column_index += 1
        for column in range(padding_count_behind):
            columns.append(Entity(column_index, 0, padding_character))
            column_index = +1
        columns.append(Entity(column_index, 0, "I"))
        return columns
