from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from friendoftech.shop.functions import get_products_and_quantities_per_user_cart
from friendoftech.shop.models import Product, CartProduct, Cart, Order, OrderProduct

UserModel = get_user_model()

# Create your views here.


class ProductListView(views.ListView):
    template_name = 'shop/product-list.html'
    paginate_by = 3
    model = Product


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

    # If you want to pass parameters to other methods by saving them to the class
    # def dispatch(self, request, *args, **kwargs):
    #     # self.cart = Cart.objects.filter(user_id=request.user.pk)
    #     self.cartproducts = CartProduct.objects.filter(cart__user_id=request.user.pk)
    #     self.products = list()
    #     self.quantitie_per_name = {}
    #     for cp in self.cartproducts:
    #         curr_product = Product.objects.filter(id=cp.product_id).get()
    #         self.products.append(curr_product)
    #         self.quantitie_per_name[curr_product.name] = cp.quantity
    #     return super(CartView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # cartproducts = CartProduct.objects.filter(cart__user_id=self.request.user.pk)
        # products = list()
        # quantities_per_name = {}
        # for cp in cartproducts:
        #     curr_product = Product.objects.filter(id=cp.product_id).get()
        #     products.append(curr_product)
        #     quantities_per_name[curr_product.name] = cp.quantity

        # Returns list(products) and dict(quantities_per_name)
        products, quantities_per_name = get_products_and_quantities_per_user_cart(self.request.user.pk)

        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['quantities_per_name'] = quantities_per_name
        return context


class CheckoutView(views.TemplateView):
    template_name = 'shop/checkout.html'

    def dispatch(self, request, *args, **kwargs):
        # Create order and orderproducts upon checkout request
        products, quantities_per_name = get_products_and_quantities_per_user_cart(request.user.pk)
        new_order = Order(user=UserModel.objects.filter(pk=request.user.pk).get())
        new_order.save()
        self.orderproducts = list()
        for product in products:
            new_orderproduct = OrderProduct(order=new_order, quantity=quantities_per_name[product.name], product=product)
            new_orderproduct.save()
            self.orderproducts.append(new_orderproduct)
            self.order = new_order
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderproducts'] = self.orderproducts
        context['order'] = self.order
        return context


def add_cart_view(request, user_pk, cartproduct_pk):
    return redirect('index')


def remove_cart_view(request, user_pk, cartproduct_pk):
    return redirect('index')


def edit_order_cart_redirect(request, order, ):

    return redirect('cart')


class CompleteOrderView(views.TemplateView):
    ...
