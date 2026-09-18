import heapq
import itertools


def dijkstra(start, goal):
    """
    Find the cheapest path from start Node to goal Node.

    Returns:
        route, total_cost

    route example:

    [
        {
            "from": Node("A"),
            "to": Node("B"),
            "type": "Blue",
            "cost": 10
        },
        {
            "from": Node("B"),
            "to": Node("D"),
            "type": "Green",
            "cost": 5
        }
    ]
    """

    distances = {
        start: 0
    }

    previous = {}

    visited = set()

    counter = itertools.count()

    queue = [
        (0, next(counter), start)
    ]

    while queue:
        current_cost, _, current_node = heapq.heappop(queue)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node is goal:
            break

        for path in current_node.possible_paths:
            neighbor = path["node"]
            path_type = path["type"]
            edge_cost = path["cost"]

            new_cost = current_cost + edge_cost

            if new_cost < distances.get(neighbor, float("inf")):

                distances[neighbor] = new_cost

                # Store everything needed to reconstruct
                # the exact route.
                previous[neighbor] = {
                    "node": current_node,
                    "type": path_type,
                    "cost": edge_cost
                }

                neighbor.reached_by = {
                    "node": current_node,
                    "type": path_type,
                    "cost": edge_cost
                }

                heapq.heappush(
                    queue,
                    (
                        new_cost,
                        next(counter),
                        neighbor
                    )
                )

    if goal not in distances:
        return None, float("inf")

    # Reconstruct route
    route = []

    current = goal

    while current is not start:
        step = previous[current]

        route.append({
            "from": step["node"],
            "to": current,
            "type": step["type"],
            "cost": step["cost"]
        })

        current = step["node"]

    route.reverse()

    return route, distances[goal]