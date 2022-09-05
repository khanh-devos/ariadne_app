
from .models import Book

# with snake_case, we can use field_name like "published_at", 
# otherwise only "publishedAt"
from ariadne import convert_kwargs_to_snake_case


@convert_kwargs_to_snake_case
def list_books(*_):
    return Book.objects.order_by("pk").reverse()[:5]


@convert_kwargs_to_snake_case
def create_book(*_, title, published_at):
    book = Book.objects.create(title =title, 
                               published_at =published_at)
    return {"title": book.title,
            "published_at": book.published_at
            }