class Map_file_reader:
    entry_character = "E"
    exit_character = "X"

    def __init__(self, lines: list[str], max_width: int, max_height: int):
        columns_out_of_bounds = filter(lambda line: len(line) > max_width, lines)
        if len(list(columns_out_of_bounds)) > 0:
            raise ValueError(
                "File has too many columns. Max column size is {}.".format(max_width)
            )

        if len(lines) > max_height:
            raise ValueError(
                "File has too many rows. Max row size is {}.".format(max_height)
            )

        has_exactly_one_entry = filter(lambda line: self.entry_character in line, lines)
        entry_point_count = len(list(has_exactly_one_entry))
        if entry_point_count != 1:
            raise ValueError(
                "File has {} entry points, but has to have exactly 1.".format(
                    entry_point_count
                )
            )

        has_exactly_one_exit = filter(lambda line: self.exit_character in line, lines)
        exit_point_count = len(list(has_exactly_one_exit))
        if exit_point_count != 1:
            raise ValueError(
                "File has {} entry points, but has to have exactly 1.".format(
                    exit_point_count
                )
            )

        map_definition = Map_Definition()
