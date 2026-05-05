from django.contrib import admin
from .models import Book, Note

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_year")

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "created_at")

