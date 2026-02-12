class Entity:
    x_position: int
    y_position: int
    ascii_symbol: str

    def __init__(self, x_position, y_position, ascii_symbol):
        self.x_position = x_position
        self.y_position = y_position
        self.ascii_symbol = ascii_symbol
