from ariadne import gql, QueryType, make_executable_schema
from ariadne_django.views import GraphQLView
from django.contrib import admin
from django.urls import path, include
import programs.urls



type_defs = gql("""
    type Query {
        hello: String!
    }
""")

def resolve_hello(*_):
    return "Hello!"

query = QueryType()
query.set_field("hello", resolve_hello)
schema = make_executable_schema(type_defs, query)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(programs.urls)),
    
    #for testing only
    path("testgraphql/", GraphQLView.as_view(schema=schema)),
]