from app import create_app
from app.extensions.database import db
from app.models import user


def create_database():
    """Script to create database with SQLAlchemy"""

    print("Instancing a Flask application context...")
    app = create_app()

    with app.app_context():
        print("Creating database...")
        db.create_all(app=app)

    print("Created!!!")
