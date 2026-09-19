import argparse

from flask import Flask, jsonify, render_template

from map_loader import load_map
from dijkstra import dijkstra


app = Flask(__name__)

MAP_FILE = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/graph")
def graph_data():
    nodes, start, goal = load_map(MAP_FILE)

    route, total_cost = dijkstra(
        start=start,
        goal=goal
    )

    # -----------------------------------
    # Nodes
    # -----------------------------------

    graph_nodes = []

    for node in nodes.values():
        graph_nodes.append({
            "id": node.name,
            "start": node is start,
            "goal": node is goal
        })

    # -----------------------------------
    # Exact edges used by shortest route
    # -----------------------------------

    route_edges = set()

    if route:
        for step in route:

            route_key = (
                step["from"].name,
                step["to"].name,
                step["type"],
                step["cost"]
            )

            route_edges.add(route_key)

    # -----------------------------------
    # Links
    # -----------------------------------
    graph_links = []
    seen = set()

    for node in nodes.values():

        for path in node.possible_paths:

            destination = path["node"]

            edge_key = (
                node.name,
                destination.name,
                path["type"],
                path["cost"]
            )

            if edge_key in seen:
                continue

            seen.add(edge_key)

            graph_links.append({
                "source": node.name,
                "target": destination.name,

                "type": path["type"].display_name,
                "color": path["type"].color,

                "cost": path["cost"],

                "shortest": edge_key in route_edges
            })

    return jsonify({
        "nodes": graph_nodes,
        "links": graph_links,
        "start": start.name,
        "goal": goal.name,
        "total_cost": (
            None
            if route is None
            else total_cost
        )
    })

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Dijkstra graph visualizer"
    )

    parser.add_argument(
        "map_file",
        help="Path to the map file"
    )

    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Web server port (default: 8000)"
    )

    args = parser.parse_args()

    MAP_FILE = args.map_file

    app.run(
        host="127.0.0.1",
        port=args.port,
        debug=True
    )