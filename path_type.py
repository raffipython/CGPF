from enum import Enum


class PathType(Enum):
    BLUE = ("Blue", 11)
    RED = ("Red", 4)
    GREEN = ("Green", 5)
    YELLOW = ("Yellow", 1)
    PURPLE = ("Purple", 9)
    ORANGE = ("Orange", 3)
    PINK = ("Pink", 8)
    CYAN = ("Cyan", 7)
    BROWN = ("Brown", 2)
    GRAY = ("Gray", 6)
    BLACK = ("Black", 10)
    TEAL = ("Teal", 12)
    MAGENTA = ("Magenta", 13)

    def __init__(self, display_name, cost):
        self.display_name = display_name

        # Default cost for this color
        self.cost = cost

    def __str__(self):
        return self.display_name