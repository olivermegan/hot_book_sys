import graphene
from graphene_django import DjangoObjectType

from hot_book_sys.hotel.models import Hotel


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel
        fields = ('id', 'name')


class Query(graphene.ObjectType):
    hotels = graphene.List(HotelType)

    def resolve_hotels(root, info):
        return Hotel.objects.all()


schema = graphene.Schema(query=Query)
