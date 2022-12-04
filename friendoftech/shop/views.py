from django.views import generic as views

from friendoftech.shop.models import Product


# Create your views here.


class ProductListView(views.ListView):
    model = Product
    template_name = 'shop/products-list.html'


class ProductDetailsView(views.DetailView):
    pass


class ProductEditView(views.CreateView):
    pass
