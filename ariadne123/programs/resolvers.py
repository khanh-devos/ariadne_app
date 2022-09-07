
from .models import Book

# with snake_case, we can use field_name like "published_at", 
# otherwise only "publishedAt"
from ariadne import convert_kwargs_to_snake_case
from ariadne_jwt.decorators import login_required
from ariadne_jwt.decorators import token_auth
import django.contrib.auth as auth
from django.contrib.auth.models import User

from ariadne_jwt import (resolve_verify, resolve_refresh, 
                         resolve_token_auth, jwt_schema)

@convert_kwargs_to_snake_case
@login_required
def list_books(_, info, token):
    try:
        request = info.context["request"]
        user = request.user
        username = resolve_verify(_, info, token)["payload"]["username"]

        print(user.username, username)
        
        if username.strip() == user.username.strip():
            return Book.objects.order_by("pk").reverse()[:5]
        else:
            return []
    except:
        return []
        
    
    




@convert_kwargs_to_snake_case
@login_required
def create_book(*_, title, published_at):
    book = Book.objects.create(title =title, 
                               published_at =published_at
                               )
    return {"title": book.title,
            "published_at": book.published_at
            }
    
def resolve_login(_, info, username, password):
    request = info.context["request"]
    user = auth.authenticate(username = username, password =password)
    
    token = resolve_token_auth(_, info, username = username, password =password)["token"]
    
    if user:
        auth.login(request, user)
        return token
    return False


def resolve_logout(_, info):
    request = info.context["request"]
    if request.user.is_authenticated:
        auth.logout(request)
        return True
    return False


@login_required
def resolve_viewer(_, info):
    return info.context.get('request').user



def create_user(*_, username, password):
    if username and len(password)>5:
        user = User.objects.create_user(username = username, password =password)
        return user
    else:
        return False
    
