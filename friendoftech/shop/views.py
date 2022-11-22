from django.views import generic as views
# Create your views here.


class ProductListView(views.ListView):
    template_name = 'shop/list_products.html'


class AddProductView(views.CreateView):
    pass


class EditProductView(views.CreateView):
    pass
