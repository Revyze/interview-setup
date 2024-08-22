from flask import Flask, jsonify, request
from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from app.hello import type_defs, query


schema = make_executable_schema(type_defs, query)

app = Flask(__name__)


# Endpoint for GraphQL queries
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


# Optional: GraphQL Explorer for testing
@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return ExplorerGraphiQL().html(None), 200


if __name__ == "__main__":
    app.run(debug=True)
