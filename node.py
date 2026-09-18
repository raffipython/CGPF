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

        if cost is None:
            cost = path_type.cost

        if cost < 0:
            raise ValueError(
                "Dijkstra cannot use negative path costs"
            )

        # Only reject an EXACT duplicate:
        #
        # same destination
        # same color
        # same cost
        #
        # Different colors between the same two nodes
        # are perfectly valid.
        for path in self.possible_paths:
            if (
                path["node"] is destination
                and path["type"] == path_type
                and path["cost"] == cost
            ):
                raise ValueError(
                    f"Duplicate path: "
                    f"{self.name} -> {destination.name} "
                    f"{path_type} ({cost})"
                )

        self.possible_paths.append({
            "node": destination,
            "type": path_type,
            "cost": cost
        })

    def __repr__(self):
        return f"Node({self.name!r})"