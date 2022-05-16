import strawberry

from app.extensions.graphql.queries import Query


def create_schema():
    return strawberry.Schema(query=Query)
