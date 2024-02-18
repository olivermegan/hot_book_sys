from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# Create your views here.

from strawberry.django.views import GraphQLView
from .schema import Query

urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=Query), name='graphql'),
]
