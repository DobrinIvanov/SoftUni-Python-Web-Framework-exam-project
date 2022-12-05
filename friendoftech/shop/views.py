from django.views import generic as views

from friendoftech.shop.models import Product


# Create your views here.


class ProductListView(views.ListView):
    model = Product
    template_name = 'shop/product-list.html'


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'shop/product-details.html'


class ProductEditView(views.CreateView):
    ...


class AddToCartView(views.View):
    ...
