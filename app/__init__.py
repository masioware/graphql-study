from flask import Flask

from app.extensions import graphql

def create_app():
    app = Flask(__name__)
    graphql.start(app)

    return app
