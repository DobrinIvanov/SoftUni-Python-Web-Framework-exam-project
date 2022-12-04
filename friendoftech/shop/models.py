from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

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

    image = models.ImageField(
        null=True,
        upload_to='images'
    )

    added = models.DateField(
        auto_now_add=True,
    )

    quantity = models.PositiveIntegerField(
        default=0,
    )

    sold = models.PositiveIntegerField(
        default=0,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)

    @property
    def in_stock(self):
        return True if self.quantity > 0 else False

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        unique=True,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        Product,
        related_name='cart',
        through='CartProduct',
    )


class CartProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    class Meta:
        unique_together = (("product", "cart"),)


# class Order(models.Model):
#     owner = models.ForeignKey(
#         AppUser,
#         on_delete=models.CASCADE,
#     )
#
#     products = models.ManyToManyField(
#         Product,
#         related_name='carts',
#         through='CartProduct',
#     )
#
#     @property
#     def total_price(self):
#         return sum([p.price for p in self.products.CartProduct])


# TODO Fix relations between Review, Product, AppUser
class Review(models.Model):
    MAX_COMMENT_LENGTH = 200

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
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
