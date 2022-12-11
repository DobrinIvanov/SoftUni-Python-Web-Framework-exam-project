from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
from friendoftech.shop.models import Product, CartProduct, Cart

UserModel = get_user_model()

# Create your views here.


class ProductListView(views.ListView):
    model = Product
    template_name = 'shop/product-list.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'shop/product-details.html'


def add_to_cart(request, product_pk, user_pk):
    product = Product.objects.filter(pk=product_pk).get()
    current_cart = Cart.objects.filter(user_id__id=user_pk).get()
    products_added = current_cart.cartproduct_set.all()
    if product.pk in [p.product_id for p in products_added]:
        existing_cartproduct = products_added.filter(product_id=product.pk).get()
        existing_cartproduct.quantity += 1
        existing_cartproduct.save()
    else:
        new_product = CartProduct(product=product, cart=current_cart)
        new_product.save()
    return redirect(reverse_lazy('product-details', kwargs={'pk': product.pk}))


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)


class CartView(views.TemplateView, LoginRequiredMixin):
    template_name = 'shop/cart.html'

    def dispatch(self, request, *args, **kwargs):
        # self.cart = Cart.objects.filter(user_id=request.user.pk)
        self.cartproducts = CartProduct.objects.filter(cart__user_id=request.user.pk)
        self.products = list()
        self.quantitie_per_name = {}
        for cp in self.cartproducts:
            curr_product = Product.objects.filter(id=cp.product_id).get()
            self.products.append(curr_product)
            self.quantitie_per_name[curr_product.name] = cp.quantity
        return super(CartView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.products
        context['quantities_per_name'] = self.quantitie_per_name
        return context


class CheckoutView(views.TemplateView):
    template_name = 'shop/checkout.html'
    #TODO