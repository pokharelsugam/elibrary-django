from django.contrib import admin
from .models import BookAuthor, BookCategory, BookPublisher, BookLanguage, Book

# Register your models here.

admin.site.register(BookAuthor) # Register BookAuthor table in admin pannel
admin.site.register(BookCategory)
admin.site.register(BookPublisher)
admin.site.register(BookLanguage)
admin.site.register(Book)