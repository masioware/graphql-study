from flask import Flask
from strawberry.flask.views import GraphQLView

from app.extensions.graphql.schema import create_schema

def start(app: Flask):
    schema = create_schema()
    view = GraphQLView.as_view(
        "graphql_view",
        schema=schema
    )

    app.add_url_rule(
        "/graphql",
        view_func=view
    )