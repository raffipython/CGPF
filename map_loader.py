from node import Node
from path_type import PathType

MAP_FILE = "map.txt"

def get_path_type(name):
    name = name.upper()

    try:
        return PathType[name]
    except KeyError:
        valid = ", ".join(path.name for path in PathType)

        raise ValueError(
            f"Unknown path type '{name}'. "
            f"Valid types: {valid}"
        )


def connect(node1, node2, path_type, cost=None):
    node1.add_path(node2, path_type, cost)
    node2.add_path(node1, path_type, cost)


def load_map():
    nodes = {}

    start_name = None
    goal_name = None

    def get_node(name):
        if name not in nodes:
            nodes[name] = Node(name)

        return nodes[name]

    with open(MAP_FILE, "r") as file:
        for line_number, raw_line in enumerate(file, start=1):

            line = raw_line.strip()

            # Ignore blank lines
            if not line:
                continue

            # Ignore full-line comments
            if line.startswith("#"):
                continue

            # Remove inline comments
            if "#" in line:
                line = line.split("#", 1)[0].strip()

            parts = line.split()

            # START
            if parts[0].upper() == "START":
                if len(parts) != 2:
                    raise ValueError(
                        f"Line {line_number}: "
                        f"START requires one node name"
                    )

                start_name = parts[1]
                get_node(start_name)
                continue

            # GOAL
            if parts[0].upper() == "GOAL":
                if len(parts) != 2:
                    raise ValueError(
                        f"Line {line_number}: "
                        f"GOAL requires one node name"
                    )

                goal_name = parts[1]
                get_node(goal_name)
                continue

            # EDGE
            if len(parts) not in (3, 4):
                raise ValueError(
                    f"Line {line_number}: expected:\n"
                    f"  NODE NODE COLOR\n"
                    f"or\n"
                    f"  NODE NODE COLOR WEIGHT"
                )

            node1_name = parts[0]
            node2_name = parts[1]
            color_name = parts[2]

            node1 = get_node(node1_name)
            node2 = get_node(node2_name)

            path_type = get_path_type(color_name)

            cost = None

            # Optional weight override
            if len(parts) == 4:
                try:
                    cost = int(parts[3])
                except ValueError:
                    raise ValueError(
                        f"Line {line_number}: "
                        f"weight must be a number"
                    )

            try:
                connect(
                    node1,
                    node2,
                    path_type,
                    cost
                )
            except ValueError as e:
                raise ValueError(
                    f"Line {line_number}: {e}"
                )

    if start_name is None:
        raise ValueError(
            "map.txt does not contain START"
        )

    if goal_name is None:
        raise ValueError(
            "map.txt does not contain GOAL"
        )

    return (
        nodes,
        nodes[start_name],
        nodes[goal_name]
    )