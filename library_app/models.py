# library_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name='User', null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    published_year = models.PositiveIntegerField(verbose_name="Publication Year")

    def __str__(self):
        return self.title

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', verbose_name='User', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='notes', verbose_name='Book', null=True, blank=True)
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f'Note for {self.book.title} by {self.user.username}'
    