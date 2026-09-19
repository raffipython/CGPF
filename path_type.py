from enum import Enum


class PathType(Enum):
    TYPE_A = ("SSH", 500, "blue")
    TYPE_B = ("TELNET", 10, "red")
    TYPE_C = ("HTTP", 2, "green")
    TYPE_D = ("HTTPS", 2, "purple")
    TYPE_F = ("RDP", 5000, "orange")
    TYPE_G = ("SMB", 5000, "pink")
    TYPE_H = ("CUSTOM", 1337, "cyan")
    TYPE_I = ("POP3", 5, "brown")
    TYPE_J = ("SMTP", 15, "gray")
    TYPE_K = ("KERB", 100, "black")
    TYPE_L = ("NETB", 100, "teal")
    TYPE_M = ("DNS", 51, "magenta")
    TYPE_N = ("CVE", 9999, "magenta")
    TYPE_X = ("Express", 4, "red")      # TEST
    TYPE_Y = ("Trail", 1, "green")      # TEST
    TYPE_Z = ("Blue Road", 11, "blue")  # TEST


    def __init__(self, display_name, cost, color):
        self.display_name = display_name
        self.cost = cost
        self.color = color

    def __str__(self):
        return self.display_name