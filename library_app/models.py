# library_app/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    author = models.CharField(max_length=100, verbose_name="Author")
    published_year = models.IntegerField(verbose_name="Publication Year")

    def __str__(self):
        return self.title
