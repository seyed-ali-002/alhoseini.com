import uuid

from django.db import models

from categories.models import Category
from posts.models import Images, Videos
from user.models import User


def slugify(url_slug):
    url_slug = url_slug.replace(" ", "-")
    url_slug = url_slug.replace(".", "-")
    url_slug = url_slug.replace(",", "-")
    url_slug = url_slug.replace("(", "-")
    url_slug = url_slug.replace(")", "")
    url_slug = url_slug.replace("؟", "")
    url_slug = url_slug.replace("?", "")
    url_slug = url_slug.replace("!", "")
    return url_slug


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    teacher = models.CharField(max_length=100, default='admin')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    images = models.ManyToManyField(Images, blank=True)
    videos = models.ManyToManyField(Videos, blank=True)
    students = models.ManyToManyField(User, blank=True)
    start_date = models.DateField(auto_now_add=True)

    course_key = models.TextField(max_length=20)

    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
