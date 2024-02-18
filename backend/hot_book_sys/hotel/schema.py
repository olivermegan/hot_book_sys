import strawberry
import typing
from strawberry.types import Info


@strawberry.type
class Room:
    floor: int
    name: str


def get_rooms() -> typing.List[Room]:
    return [
        Room(floor=1, name="room1"),
        Room(floor=2, name="room2"),
    ]


@strawberry.type
class Query:
    rooms: typing.List[Room] = strawberry.field(resolver=get_rooms)


def get_room():
    return [
        Room(floor=1, name="room1"),
        Room(floor=2, name="room2"),
    ]


schema = strawberry.Schema(query=Query)
