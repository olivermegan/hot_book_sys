import strawberry
import typing
from . import Room
from strawberry_django.optimizer import DjangoOptimizerExtension
from .resolvers import get_rooms
from strawberry.types import Room


@strawberry.type
class Query:
    rooms: typing.List[Room] = strawberry_django.field(resolver=get_rooms)


schema = strawberry.Schema(
    query=Query,
    extensions=[
        DjangoOptimizerExtension
    ]
)
