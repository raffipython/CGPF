from map_loader import load_map
from dijkstra import dijkstra


def main():
    try:
        nodes, start, goal = load_map()

    except FileNotFoundError:
        print("Error: map.txt was not found.")
        return

    except ValueError as e:
        print(f"Map error: {e}")
        return

    route, total_cost = dijkstra(
        start=start,
        goal=goal
    )

    if route is None:
        print(
            f"No path from {start.name} "
            f"to {goal.name}."
        )
        return

    print(
        f"Shortest route from "
        f"{start.name} to {goal.name}:"
    )
    print()

    for step in route:
        print(
            f"{step['from'].name} "
            f"--{step['type']} "
            f"({step['cost']})--> "
            f"{step['to'].name}"
        )

    print()
    print("Total cost:", total_cost)


if __name__ == "__main__":
    main()