from django.core.validators import MinValueValidator
from django.db import models
from django.template.defaultfilters import slugify

from friendoftech.accounts.models import AppUser
from friendoftech.shop.enums import Category

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Product(models.Model):
    MAX_PRODUCT_NAME_LENGTH = 150

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


# Signal to create Cart when User is registered.
@receiver(post_save, sender=AppUser)
def create_cart_signal(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)
    instance.cart.save()


class Order(models.Model):
    user = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    products = models.ManyToManyField(
        Product,
        related_name='carts',
        through='OrderProduct',
    )

    shipping_address = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    phone_nr = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    comment = models.TextField(
        null=True,
        blank=True,
    )

    is_completed = models.BooleanField(
        default=False,
    )

    is_submited = models.BooleanField(
        default=False,
    )

    @property
    def total_price(self):
        return sum([p.product.price for p in self.orderproduct_set])


class OrderProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    class Meta:
        unique_together = ["product", "order"]


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


class Review(models.Model):
    MAX_COMMENT_LENGTH = 300

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
