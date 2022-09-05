
from ariadne_django.views import GraphQLView
from .graphql_config import schema
from django.urls import path


urlpatterns = [
    path("graphql/", GraphQLView.as_view(schema=schema), name="programs"),
]