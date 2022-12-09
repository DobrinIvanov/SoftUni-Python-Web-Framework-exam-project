from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from friendoftech.shop.models import Product, Cart

UserModel = get_user_model()

# Create your views here.


class ProductListView(views.ListView):
    model = Product
    template_name = 'shop/product-list.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'shop/product-details.html'


class CartView(views.TemplateView):
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs):
        super().get_context_data(**kwargs)


def add_to_cart_old(request, product_pk, user_pk):
    product = Product.objects.filter(pk=product_pk).get()
    user = UserModel.objects.filter(pk=user_pk).get()

    context = {
        'product': product,
        'user': user,
    }
    return render(request, 'shop/cart.html', context)


def add_to_cart(request, product_pk, user_pk):
    product = Product.objects.filter(pk=product_pk).get()
    Cart.objects.filter(user_id__id=user_pk).get().products.add(product)

    return redirect(reverse_lazy('product-details', kwargs={'pk': product.pk}))


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
