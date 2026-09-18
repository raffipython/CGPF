from flask import Flask, jsonify, render_template

from map_loader import load_map
from dijkstra import dijkstra


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/graph")
def graph_data():
    nodes, start, goal = load_map()

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

            endpoints = tuple(sorted([
                step["from"].name,
                step["to"].name
            ]))

            route_key = (
                endpoints[0],
                endpoints[1],
                str(step["type"]),
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

            endpoints = tuple(sorted([
                node.name,
                destination.name
            ]))

            edge_key = (
                endpoints[0],
                endpoints[1],
                str(path["type"]),
                path["cost"]
            )

            # Skip only the reverse copy of the
            # exact same edge.
            if edge_key in seen:
                continue

            seen.add(edge_key)

            graph_links.append({
                "source": node.name,
                "target": destination.name,

                # User-facing path name
                "type": path["type"].display_name,

                # Actual CSS/D3 color
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
    app.run(
        debug=True,
        port=8000
    )