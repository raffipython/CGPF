from enum import Enum


class PathType(Enum):
    BLUE = ("Blue", 10)
    RED = ("Red", 20)
    GREEN = ("Green", 5)
    YELLOW = ("Yellow", 15)

    def __init__(self, display_name, cost):
        self.display_name = display_name
        self.cost = cost

    def __str__(self):
        return self.display_name