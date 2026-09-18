from path_type import PathType


class Node:
    def __init__(self, name):
        self.name = name
        self.reached_by = None
        self.possible_paths = []

    def add_path(self, destination, path_type, cost=None):
        if not isinstance(path_type, PathType):
            raise TypeError(
                f"path_type must be a PathType, got {path_type!r}"
            )

        # Use the color's default cost if one wasn't supplied
        if cost is None:
            cost = path_type.cost

        if cost < 0:
            raise ValueError(
                "Dijkstra cannot use negative path costs"
            )

        # A node cannot have two paths with the same color
        for path in self.possible_paths:
            if path["type"] == path_type:
                raise ValueError(
                    f"Node {self.name} already has a "
                    f"{path_type} path"
                )

        self.possible_paths.append({
            "node": destination,
            "type": path_type,
            "cost": cost
        })

    def __repr__(self):
        return f"Node({self.name!r})"