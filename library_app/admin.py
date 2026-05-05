from django.contrib import admin
from .models import Book, Note

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
    fields = ('user', 'text', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_year")
    inlines = [NoteInline]

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("book", "user", "created_at")

