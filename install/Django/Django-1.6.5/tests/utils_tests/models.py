from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __next__(self):
        return self


class Thing(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
