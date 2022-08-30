from django.db import models

from .category import Category


class Product(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ManyToManyField(Category, blank=True)
