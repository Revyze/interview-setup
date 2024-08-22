from ariadne import QueryType

# GraphQL schema
type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()


@query.field("hello")
def resolve_hello(_, info):
    return "Hello World"
