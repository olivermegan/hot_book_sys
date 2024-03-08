import graphene
from graphene_django import DjangoObjectType

from hot_book_sys.hotel.models import Hotel


class HotelType(DjangoObjectType):
    class Meta:
        model = Hotel
        fields = ('id', 'name')


class Query(graphene.ObjectType):
    hotels = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
