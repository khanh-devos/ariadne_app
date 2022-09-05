from django.contrib import admin

from .models import Book,Program
# Register your models here.
admin.site.register(Program)
admin.site.register(Book)
