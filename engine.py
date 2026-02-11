import time
from foe import Foe


class Engine:
    def __init__(self, tick_interval_in_seconds):
        self.tick_interval_in_seconds = tick_interval_in_seconds

    def start(self):
        while True:
            time.sleep(self.tick_interval_in_seconds)
            Engine.draw_Map()

    @staticmethod
    def draw_Map():
        Engine.hide_cursor()
        Engine.reset_cursor()
        Engine.clear_screen()
        Engine.draw_Border()

    @staticmethod
    def move_cursor(x, y):
        print("\033[{};{}H".format(y, x), end="")

    @staticmethod
    def reset_cursor():
        print("\033[H", end="")

    @staticmethod
    def clear_screen():
        print("\033[J", end="")

    @staticmethod
    def hide_cursor():
        print("\033[?25l", end="")

    @staticmethod
    def show_cursor():
        print("\033[?25h", end="")

    @staticmethod
    def move_Entity(foe: Foe, x: int, y: int):
        Engine.move_cursor(foe.x_position, foe.y_position)
        print(" ")
        Engine.move_cursor(x, y)
        print(foe.asciiSymbol)
        Engine.hide_cursor()
        foe.x_position = x
        foe.y_position = y

    @staticmethod
    def draw_Border():
        columns: int = 80
        rows: int = 30
        title: str = "ASCII TOWER DEFENSE"
        # I want to center the title on the top border
        columns_minus_title = columns - len(title)
        columns_before_title = columns_minus_title // 2 + columns_minus_title % 2
        columns_after_title = columns_minus_title // 2

        for column in range(columns_before_title):
            print("=", end="")
        print(title, end="")
        for column in range(columns_after_title):
            print("=", end="")
        print()

        for row in range(1, rows):  # (1, rows):
            for column in range(columns):
                if row == rows - 1:
                    print("=", end="")
                    continue
                if column == 0 or column == columns - 1:
                    print("I", end="")
                    continue
                print(" ", end="")
            print()
