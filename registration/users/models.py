from django.db import models
from django.contrib.auth.models import AbstractUser


class Label(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class User(AbstractUser):
    label =  models.ForeignKey(
        Label,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
    )
