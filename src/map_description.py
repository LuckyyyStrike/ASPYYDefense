class MapDescription:
    # TODO
    # Lines have to be normalized by taking the longest line,
    # trim it at front and end and trim all other lines by the
    # same amount to make sure that the entities don't misalign

    # def __init__(self, width: int, height: int, lines: list[str]) -> None:
    def __init__(self, lines: list[str]) -> None:
        # self.width = width
        # self.height = height
        self.lines = lines
