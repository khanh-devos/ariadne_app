from ariadne import (QueryType, make_executable_schema, 
                     snake_case_fallback_resolvers, 
                     load_schema_from_path, MutationType)

import programs.resolvers
from ariadne_django.scalars import date_scalar, datetime_scalar

type_defs = [
    load_schema_from_path("programs/schema.graphql")
]

query = QueryType()
query.set_field("books", programs.resolvers.list_books)

mutation = MutationType()
mutation.set_field("create_book", programs.resolvers.create_book)

schema = make_executable_schema(type_defs, query, mutation, 
                                date_scalar,
                                datetime_scalar,
                                snake_case_fallback_resolvers)