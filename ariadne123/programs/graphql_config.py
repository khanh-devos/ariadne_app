from ariadne import (QueryType, make_executable_schema, 
                     snake_case_fallback_resolvers, upload_scalar,
                     load_schema_from_path, MutationType)

import programs.resolvers
from ariadne_django.scalars import date_scalar, datetime_scalar

from ariadne_jwt import (resolve_verify, resolve_refresh, 
                         resolve_token_auth, jwt_schema)

type_defs = [
    load_schema_from_path("programs/schema.graphql")
]

query = QueryType()
query.set_field("books", programs.resolvers.list_books)
query.set_field("me", programs.resolvers.resolve_viewer)


mutation = MutationType()
mutation.set_field("create_book", programs.resolvers.create_book)

# For ariadne-jwt
mutation.set_field('verifyToken', resolve_verify)
mutation.set_field('refreshToken', resolve_refresh)
mutation.set_field('tokenAuth', resolve_token_auth)

mutation.set_field("login", programs.resolvers.resolve_login)
mutation.set_field("logout", programs.resolvers.resolve_logout)
mutation.set_field("create_user", programs.resolvers.create_user)


schema = make_executable_schema(type_defs, query, mutation, 
                                date_scalar,
                                datetime_scalar,
                                upload_scalar,
                                snake_case_fallback_resolvers)