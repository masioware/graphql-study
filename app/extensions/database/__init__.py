from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def start(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    db.init_app(app)
