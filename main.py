import heapq


def dijkstra(graph, start, goal):
    # Best known distance from start to each node
    distances = {start: 0}

    # Used to reconstruct the final path
    previous = {}

    # Priority queue entries are:
    # (distance_from_start, node)
    queue = [(0, start)]

    # Keep track of nodes whose shortest distance is finalized
    visited = set()

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Skip nodes we've already finalized
        if current_node in visited:
            continue

        visited.add(current_node)

        # If we reached the goal, we're done
        if current_node == goal:
            break

        # Check all neighbors
        for neighbor, weight in graph.get(current_node, []):
            if weight < 0:
                raise ValueError("Dijkstra cannot use negative edge weights")

            new_distance = current_distance + weight

            # If this is a better route, save it
            if new_distance < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    queue,
                    (new_distance, neighbor)
                )

    # Goal was never reached
    if goal not in distances:
        return None, float("inf")

    # Reconstruct path
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = previous[node]

    path.append(start)
    path.reverse()

    return path, distances[goal]


#        4
#   A ------- B
#   |         |
#  2|         |3
#   |         |
#   C ------- D
#        1


graph = {
    "A": [
        ("B", 4),
        ("C", 2)
    ],

    "B": [
        ("A", 4),
        ("D", 3)
    ],

    "C": [
        ("A", 2),
        ("D", 1)
    ],

    "D": [
        ("B", 3),
        ("C", 1)
    ]
}

path, cost = dijkstra(graph, "A", "D")

print("Path:", path)
print("Cost:", cost)


