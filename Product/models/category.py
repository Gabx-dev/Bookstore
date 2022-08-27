from django.db import models


class Category(models.Model):
  title = models.CharField(max_length=255, unique=True)
  slug = models.SlugField(max_length=255, unique=True)
  description = models.TextField(blank=True)
  active = models.BooleanField(default=True)