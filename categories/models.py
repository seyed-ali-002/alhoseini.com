from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.TextField(max_length=200)
    url = models.TextField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
