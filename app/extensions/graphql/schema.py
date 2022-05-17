from typing import List

import strawberry

from app.extensions.graphql.queries import show_all_users


@strawberry.type
class User:
    id: int
    username: str
    email: str


@strawberry.type
class Query:
    get_users: List[User] = strawberry.field(resolver=show_all_users)


def create_schema():
    return strawberry.Schema(query=Query)
