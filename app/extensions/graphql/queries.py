from app.models.user import User


def show_all_users():
    return User.query.all()
