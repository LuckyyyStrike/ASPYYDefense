import time
from foe import Foe


def move_cursor(x, y):
    print("\033[{};{}H".format(y, x), end="")


def reset_cursor():
    print("\033[H", end="")


def clear_screen():
    print("\033[J", end="")


def hide_cursor():
    print("\033[?25l", end="")


def show_cursor():
    print("\033[?25h", end="")


def moveEntity(foe, x, y):
    move_cursor(foe.xPosition, foe.yPosition)
    print(" ")
    move_cursor(x, y)
    print(foe.asciiSymbol)
    hide_cursor()


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


y = 10
x = 3

doLoop = True
while doLoop:
    time.sleep(1)
    hide_cursor()
    reset_cursor()
    clear_screen()
    drawBorder()
    foe1 = Foe()
    moveEntity(foe1, x, y)
    x += 1
