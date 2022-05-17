from flask import Flask

from app.extensions import database
from app.extensions import graphql


def create_app():
    app = Flask(__name__)

    database.start(app)
    graphql.start(app)

    return app
