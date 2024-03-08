import graphene


class Query(graphene.ObjectType):
    hotels = graphene.String(default_value="Hi!")


schema = graphene.Schema(query=Query)
