import time
from foe import Foe


class Engine:
    def __init__(self, tickrateInSeconds):
        self.tickrateInSeconds = tickrateInSeconds

    def start(self):
        doLoop = True
        while doLoop:
            time.sleep(self.tickrateInSeconds)
            Engine.drawMap()

    @staticmethod
    def drawMap():
        Engine.hide_cursor()
        Engine.reset_cursor()
        Engine.clear_screen()
        Engine.drawBorder()

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
    def moveEntity(foe: Foe, x: int, y: int):
        Engine.move_cursor(foe.xPosition, foe.yPosition)
        print(" ")
        Engine.move_cursor(x, y)
        print(foe.asciiSymbol)
        Engine.hide_cursor()
        foe.xPosition = x
        foe.yPosition = y

    @staticmethod
    def drawBorder():
        columns: int = 80
        rows: int = 30
        title: str = "ASCII TOWER DEFENSE"
        # I want to center the title on the top border
        columnsMinusTitle = columns - len(title)
        columnsBeforeTitle = columnsMinusTitle // 2 + columnsMinusTitle % 2
        columnsAfterTitle = columnsMinusTitle // 2

        for column in range(columnsBeforeTitle):
            print("=", end="")
        print(title, end="")
        for column in range(columnsAfterTitle):
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
