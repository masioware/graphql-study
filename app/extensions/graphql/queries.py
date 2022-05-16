import strawberry

@strawberry.type
class Query:
    @strawberry.field
    def hello(name: str) -> str:
        return f"Hello {name}"

