from django.db import models

from friendoftech.accounts.models import AppUser


# Create your models here.
class Article(models.Model):
    title = models.CharField(
        max_length=40,
        null=False,
        blank=False,
    )

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    summary = models.CharField(
        max_length=75,
        null=False,
        blank=False,
    )

    content = models.TextField(
        null=False,
        blank=False,
    )

    # TODO work on images, how they are stored, etc.
    image = models.ImageField(
        null=True,
    )

    def __str__(self):
        return f'{self.title}'
