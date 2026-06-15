from django.db import models
from django.utils.html import strip_tags
from imagekit.models import ImageSpecField
from ckeditor_uploader.fields import RichTextUploadingField

from categories.models import Category
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

class Images(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='uploads/images/')
    thumbnail = ImageSpecField(
        source='image',
        options={'quality': 90}
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name == "":
            self.name = self.image.name

            self.name = self.name.replace(" ", "-")
            self.name = self.name.replace(".jpg", "")
            self.name = self.name.replace(".jpeg", "")
            self.name = self.name.replace(".png", "")
            self.name = self.name.replace(".webp", "")

        super().save(*args, **kwargs)


class Videos(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=True)
    url = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, null=True, blank=True)
    # todo: short url for sharing
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    image = models.ForeignKey(Images, on_delete=models.SET_NULL, null=True)
    views = models.PositiveIntegerField(default=0, blank=True)
    body = RichTextUploadingField(null=True, blank=True)
    summary = models.TextField(max_length=300, blank=True)

    published = models.BooleanField(default=False)
    published_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.summary:
            plain_text = strip_tags(self.body)
            self.summary = plain_text[:270]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
