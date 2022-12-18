from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

from friendoftech.shop.forms import WriteReviewForm
from friendoftech.shop.functions import get_products_and_quantities_per_user_cart
from friendoftech.shop.models import Product, CartProduct, Cart, Order, OrderProduct
from guardian import mixins as guardian_mixins

UserModel = get_user_model()

# Create your views here.


class ProductListView(views.ListView):
    template_name = 'shop/product-list.html'
    paginate_by = 3
    model = Product


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'shop/product-details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        reviews = product.review_set.all()
        context['reviews'] = reviews
        return context


@login_required
def add_to_cart(request, pk, product_pk):
    if not pk == request.user.pk:
        return redirect('sign-in')
    product = Product.objects.filter(pk=product_pk).get()
    current_cart = Cart.objects.filter(user_id__id=pk).get()
    products_added = current_cart.cartproduct_set.all()
    if product.pk in [p.product_id for p in products_added]:
        existing_cartproduct = products_added.filter(product_id=product.pk).get()
        existing_cartproduct.quantity += 1
        existing_cartproduct.save()
    else:
        new_product = CartProduct(product=product, cart=current_cart)
        new_product.save()
    return redirect(reverse_lazy('product-details', kwargs={'pk': product_pk}))


class CartView(views.TemplateView, LoginRequiredMixin):
    template_name = 'shop/cart.html'

    def get_context_data(self, **kwargs):
        products, quantities_per_name = get_products_and_quantities_per_user_cart(self.request.user.pk)
        context = super().get_context_data(**kwargs)
        context['products'] = products
        context['quantities_per_name'] = quantities_per_name
        return context


class CheckoutView(views.TemplateView, LoginRequiredMixin):
    template_name = 'shop/checkout.html'

    def dispatch(self, request, *args, **kwargs):

        # Create order and orderproducts upon checkout request
        products, quantities_per_name = get_products_and_quantities_per_user_cart(request.user.pk)
        if not products:
            return redirect('index')
        new_order = Order(user=UserModel.objects.filter(pk=request.user.pk).get())
        new_order.save()

        self.orderproducts = list()
        for product in products:
            new_orderproduct = OrderProduct(
                order=new_order,
                quantity=quantities_per_name[product.name],
                product=product
            )
            new_orderproduct.save()
            self.orderproducts.append(new_orderproduct)
            self.order = new_order

        return super(CheckoutView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderproducts'] = self.orderproducts
        context['order'] = self.order
        return context


def add_cartproduct_view(request, pk, pid):
    if not pk == request.user.pk:
        return redirect('sign-in')
    cart_id = Cart.objects.filter(user_id=pk).get().pk
    cartproduct = CartProduct.objects.filter(cart_id=cart_id).filter(product_id=pid).get()
    cartproduct.quantity += 1
    cartproduct.save()
    return redirect('cart', pk=pk)


def remove_cartproduct_view(request, pk, pid):
    if not pk == request.user.pk:
        return redirect('sign-in')
    cart_id = Cart.objects.filter(user_id=pk).get().pk
    cartproduct = CartProduct.objects.filter(cart_id=cart_id, product_id=pid).get()
    if cartproduct.quantity == 1:
        cartproduct.delete()
    else:
        cartproduct.quantity -= 1
        cartproduct.save()
    return redirect('cart', pk=pk)


def edit_order_cart_redirect(request, userpk, orderid):
    Order.objects.filter(pk=orderid).get().delete()
    return redirect('cart', pk=userpk)


class CompleteOrderView(views.TemplateView):
    template_name = 'shop/complete-order.html'

    def dispatch(self, request, *args, **kwargs):
        # userpk = self.kwargs['pk']
        self.orderid = self.kwargs['orderid']
        curr_order = Order.objects.filter(id=self.orderid).get()
        curr_order.is_submited = True
        return super(CompleteOrderView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orderid'] = self.orderid
        return context


class WriteReview(views.CreateView, LoginRequiredMixin):
    template_name = 'shop/write-review.html'
    form_class = WriteReviewForm
    success_url = reverse_lazy('product-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_id = self.kwargs['pid']
        # user_pk = self.kwargs['pk']
        product = Product.objects.filter(id=product_id).get()
        context['product'] = product
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.product_id = self.kwargs['pid']
        return super(WriteReview, self).form_valid(form)
