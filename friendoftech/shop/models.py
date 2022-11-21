from django.core.validators import MinValueValidator
from django.db import models

from friendoftech.accounts.models import AppUser
from friendoftech.shop.enums import Category


# Create your models here.


class Product(models.Model):
    MAX_PRODUCT_NAME_LENGTH = 60

    name = models.CharField(
        max_length=MAX_PRODUCT_NAME_LENGTH,
        blank=False,
        null=False,
    )

    category = models.CharField(
        choices=Category.choices(),
        null=True,
        blank=True,
        max_length=50,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[MinValueValidator(0), ]
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    added = models.DateField(
        auto_now_add=True,
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    @property
    def in_stock(self):
        return True if self.quantity > 0 else False


class Review(models.Model):
    MAX_COMMENT_LENGTH = 200

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    author = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    added = models.DateTimeField(
        auto_now_add=True,
    )

    comment = models.TextField(
        max_length=MAX_COMMENT_LENGTH,
        null=False,
        blank=False,
    )

    is_positive = models.BooleanField(
        null=False,
        blank=False,
    )
