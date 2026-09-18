from enum import Enum


class PathType(Enum):
    TYPE_A = ("Blue Road", 11, "blue")
    TYPE_B = ("Express Route", 4, "red")
    TYPE_C = ("Forest Path", 5, "green")
    TYPE_D = ("Trail", 1, "yellow")
    TYPE_E = ("Tunnel", 9, "purple")
    TYPE_F = ("Bridge", 3, "orange")
    TYPE_G = ("Side Road", 8, "pink")
    TYPE_H = ("River Path", 7, "cyan")
    TYPE_I = ("Dirt Road", 2, "brown")
    TYPE_J = ("Stone Road", 6, "gray")
    TYPE_K = ("Railway", 10, "black")
    TYPE_L = ("Coastal Road", 12, "teal")
    TYPE_M = ("Mountain Pass", 13, "magenta")

    def __init__(self, display_name, cost, color):
        self.display_name = display_name
        self.cost = cost
        self.color = color

    def __str__(self):
        return self.display_name