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
    # Determine which edges are part of
    # the shortest route
    # -----------------------------------

    route_edges = set()

    if route:
        for step in route:
            key = tuple(sorted([
                step["from"].name,
                step["to"].name
            ]))

            route_edges.add(key)

    # -----------------------------------
    # Links
    #
    # Each undirected connection exists
    # twice internally:
    #
    # A -> B
    # B -> A
    #
    # D3 only needs it once.
    # -----------------------------------

    graph_links = []
    seen = set()

    for node in nodes.values():

        for path in node.possible_paths:
            destination = path["node"]

            edge_key = tuple(sorted([
                node.name,
                destination.name
            ]))

            if edge_key in seen:
                continue

            seen.add(edge_key)

            graph_links.append({
                "source": node.name,
                "target": destination.name,
                "type": str(path["type"]),
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