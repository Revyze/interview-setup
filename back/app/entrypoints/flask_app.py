from ariadne import graphql_sync, make_executable_schema
from ariadne.explorer import ExplorerGraphiQL
from flask import Flask, jsonify, request
from flask_cors import CORS

from app.entrypoints.base_gql_types import query, type_defs

schema = make_executable_schema(type_defs, query)

app = Flask(__name__)
CORS(app)


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema, data, context_value={"request": request}, debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code


@app.route("/graphql", methods=["GET"])
def graphql_explorer():
    return ExplorerGraphiQL().html(None), 200


if __name__ == "__main__":
    app.run(debug=True)
