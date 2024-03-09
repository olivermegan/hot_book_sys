import graphene
from graphene_django import DjangoObjectType

from hot_book_sys.hotel.models import Hotel, Room


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel
        fields = "__all__"


class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        fields = "__all__"


class Query(graphene.ObjectType):
    hotels = graphene.List(HotelType)
    rooms = graphene.List(RoomType)

    def resolve_hotels(root, info):
        return Hotel.objects.all()

    def resolve_rooms(root, info):
        return Room.objects.all()


schema = graphene.Schema(query=Query)
