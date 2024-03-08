from strawberry.django.views import GraphQLView
from .schema import schema
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
# from django.http import JsonResponse

# Create your views here.


urlpatterns = [
    path('graphql/', GraphQLView.as_view(schema=schema), name='graphql'),
]
