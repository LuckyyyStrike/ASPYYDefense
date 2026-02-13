from map import Map


class MapRenderer:
    @staticmethod
    def render_map(map: Map):
        MapRenderer.clear_screen()
        MapRenderer.reset_cursor()

        for row in map._matrix:
            row_symbols = "".join([c.ascii_symbol for c in row])
            print(row_symbols)

        MapRenderer.hide_cursor()

    @staticmethod
    def move_cursor(x, y):
        print("\033[{};{}H".format(y, x), end="")

    @staticmethod
    def reset_cursor():
        print("\033[H", end="")

    @staticmethod
    def clear_screen():
        print("\033[2J", end="")

    @staticmethod
    def hide_cursor():
        print("\033[?25l", end="")

    @staticmethod
    def show_cursor():
        print("\033[?25h", end="")
