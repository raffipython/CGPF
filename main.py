from node import Node
from path_type import PathType
from dijkstra import dijkstra


def connect(node1, node2, path_type, cost=None):
    """
    Create an undirected path.

    If cost is omitted, PathType's default cost is used.

    Example:
        connect(a, b, PathType.BLUE)

    BLUE defaults to 11, so this creates:

        A --Blue(11)-- B
    """

    node1.add_path(node2, path_type, cost)
    node2.add_path(node1, path_type, cost)


def main():

    # --------------------------------------------------
    # Create nodes
    # --------------------------------------------------

    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")
    h = Node("H")
    i = Node("I")
    j = Node("J")
    k = Node("K")
    l = Node("L")
    m = Node("M")

    # --------------------------------------------------
    # Build graph
    # --------------------------------------------------

    # ----------------
    # Top
    # ----------------

    # BLUE default = 11
    connect(a, b, PathType.BLUE)

    # RED default = 4
    connect(a, d, PathType.RED)

    # PINK default = 8
    connect(a, c, PathType.PINK)

    # MAGENTA default = 13
    connect(a, m, PathType.MAGENTA)

    # RED default = 4
    connect(b, c, PathType.RED)

    # PURPLE default = 9
    connect(b, m, PathType.PURPLE)

    # TEAL default = 12
    connect(b, g, PathType.TEAL)

    # GREEN default = 5
    connect(c, m, PathType.GREEN)

    # ----------------
    # Left side
    # ----------------

    # YELLOW default = 1
    connect(d, m, PathType.YELLOW)

    # ORANGE default = 3
    connect(d, f, PathType.ORANGE)

    # GRAY default = 6
    connect(d, e, PathType.GRAY)

    # TEAL normally = 12
    # This specific edge has weight 3
    connect(f, m, PathType.TEAL, 3)

    # GREEN default = 5
    connect(e, f, PathType.GREEN)

    # ORANGE normally = 3
    # This specific edge has weight 9
    connect(e, m, PathType.ORANGE, 9)

    # BROWN default = 2
    connect(e, j, PathType.BROWN)

    # ----------------
    # Right side
    # ----------------

    # BLUE normally = 11
    # This specific edge has weight 5
    connect(m, g, PathType.BLUE, 5)

    # CYAN default = 7
    connect(m, i, PathType.CYAN)

    # BROWN default = 2
    connect(m, h, PathType.BROWN)

    # PINK default = 8
    connect(i, g, PathType.PINK)

    # BLACK default = 10
    connect(i, h, PathType.BLACK)

    # YELLOW default = 1
    connect(g, h, PathType.YELLOW)

    # ----------------
    # Bottom
    # ----------------

    # GRAY normally = 6
    # This specific edge has weight 1
    connect(m, j, PathType.GRAY, 1)

    # RED normally = 4
    # This specific edge has weight 9
    connect(m, l, PathType.RED, 9)

    # BLACK default = 10
    connect(m, k, PathType.BLACK)

    # PINK default = 8
    connect(j, l, PathType.PINK)

    # ORANGE default = 3
    connect(l, k, PathType.ORANGE)

    # GREEN default = 5
    connect(j, k, PathType.GREEN)

    # PINK default = 8
    connect(k, h, PathType.PINK)

    # --------------------------------------------------
    # Run Dijkstra
    # --------------------------------------------------

    start = f
    goal = h

    route, total_cost = dijkstra(
        start=start,
        goal=goal
    )

    if route is None:
        print("No path found.")
        return

    print(
        f"Shortest route from "
        f"{start.name} to {goal.name}:"
    )

    print()

    for step in route:
        print(
            f"{step['from'].name} "
            f"--{step['type']} ({step['cost']})--> "
            f"{step['to'].name}"
        )

    print()
    print("Total cost:", total_cost)


if __name__ == "__main__":
    main()