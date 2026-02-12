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

        # We want to center the map area vertically
        padding_rows_count = max_height - len(map_description.lines)
        padding_rows_infront = padding_rows_count // 2
        padding_rows_after = padding_rows_infront + padding_rows_count % 2

        first_row = self.create_centered_row(Literals.border_title, 0, "=")
        self._matrix.append(first_row)
        row_index: int = 1
        for row in range(padding_rows_infront - 1):
            padded_row = self.create_centered_row("", row_index, " ")
            self._matrix.append(padded_row)
            row_index += 1
        for map_line in map_description.lines:
            padded_row = self.create_centered_row(map_line, row_index, " ")
            self._matrix.append(padded_row)
            row_index += 1
        for row in range(padding_rows_after - 1):
            padded_row = self.create_centered_row("", row_index, " ")
            self._matrix.append(padded_row)
            row_index += 1
        last_row = self.create_centered_row("", row_index, "=")
        self._matrix.append(last_row)

    def create_centered_row(self, content: str, row_index: int, padding_character: str):
        columns_minus_content = self.max_width - len(content) - 2
        columns_before_content = columns_minus_content // 2 + columns_minus_content % 2
        columns_after_content = columns_minus_content // 2

        columns: list[Entity] = [Entity(0, row_index, "I")]
        column_index = 1
        for column in range(columns_before_content):
            columns.append(Entity(column_index, 0, padding_character))
            column_index += 1
        for content_character in content:
            columns.append(Entity(column_index, 0, content_character))
            column_index += 1
        for column in range(columns_after_content):
            columns.append(Entity(column_index, 0, padding_character))
            column_index = +1
        columns.append(Entity(column_index, 0, "I"))
        return columns
