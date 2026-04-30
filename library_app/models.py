# library_app/models.py
from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', verbose_name='User')
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    published_year = models.PositiveIntegerField(verbose_name="Publication Year")

    def __str__(self):
        return self.title
