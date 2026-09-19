from node import Node
from path_type import PathType

def get_path_type(name):
    """
    Find a PathType by its display name.

    Examples:
        "Express Route"
        "Forest Path"
        "Blue Road"

    Matching is case-insensitive.
    """

    name = name.strip().lower()

    for path_type in PathType:
        if path_type.display_name.lower() == name:
            return path_type

    valid = ", ".join(
        path.display_name
        for path in PathType
    )

    raise ValueError(
        f"Unknown path type '{name}'. "
        f"Valid types: {valid}"
    )


def connect(node1, node2, path_type, cost=None):
    """
    Create a directional connection.

    node1 -> node2
    """

    node1.add_path(node2, path_type, cost)


def load_map(map_file):
    nodes = {}

    start_name = None
    goal_name = None

    seen_edges = set()

    def get_node(name):
        if name not in nodes:
            nodes[name] = Node(name)

        return nodes[name]

    with open(map_file, "r") as file:

        for line_number, raw_line in enumerate(
            file,
            start=1
        ):

            line = raw_line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            if "#" in line:
                line = line.split("#", 1)[0].strip()

            parts = line.split()

            if parts[0].upper() == "START":
                start_name = parts[1]
                get_node(start_name)
                continue

            if parts[0].upper() == "GOAL":
                goal_name = parts[1]
                get_node(goal_name)
                continue

           # We need at least:
            #
            # NODE NODE PATH_TYPE
            #
            # Example:
            #
            # A B Express Route
            #
            if len(parts) < 3:
                raise ValueError(
                    f"Line {line_number}: expected:\n"
                    f"  NODE NODE PATH TYPE\n"
                    f"or\n"
                    f"  NODE NODE PATH TYPE WEIGHT"
                )

            node1_name = parts[0]
            node2_name = parts[1]

            node1 = get_node(node1_name)
            node2 = get_node(node2_name)


            # --------------------------------------------------
            # Determine whether the final value is a weight
            # --------------------------------------------------

            cost = None

            try:
                cost = int(parts[-1])

                # Everything between the node names and
                # the final number is the path name.
                path_name = " ".join(
                    parts[2:-1]
                )

            except ValueError:

                # No numeric weight was supplied.
                # Everything after the two node names
                # is the path name.
                path_name = " ".join(
                    parts[2:]
                )


            if not path_name:
                raise ValueError(
                    f"Line {line_number}: "
                    f"path type is missing"
                )


            path_type = get_path_type(
                path_name
            )

            actual_cost = (
                path_type.cost
                if cost is None
                else cost
            )

            edge_key = (
                node1_name,
                node2_name,
                path_type,
                actual_cost
            )
            
            # Exact duplicate/reverse duplicate
            if edge_key in seen_edges:
                continue

            seen_edges.add(edge_key)

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