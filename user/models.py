from django.contrib.auth.models import AbstractUser
from django.db import models

role = [
    ("admin", 'admin'),
    ("member", 'member')
]


# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11)
    permission = models.CharField(choices=role, default='member', max_length=10)

    def save(
            self,
            *,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        if self.permission == 'admin' and not self.is_superuser:
            self.is_superuser = True

    # def __str__(self):
    #     return self.get_full_name()
