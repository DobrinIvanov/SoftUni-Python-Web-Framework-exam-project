from django.contrib import admin

from friendoftech.shop.models import Product, Review, Cart, CartProduct


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'is_positive', 'author')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    pass
