from django.db import models


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now=True)
    author = models.ManyToManyField('Author')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
