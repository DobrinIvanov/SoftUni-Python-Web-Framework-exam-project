from django.contrib.auth import get_user_model
from friendoftech.shop.models import CartProduct, Product, OrderProduct

UserModel = get_user_model()


def get_products_and_quantities_per_user_cart(user_pk):
    cartproducts = CartProduct.objects.filter(cart__user_id=user_pk)
    products = list()
    quantities_per_name = {}
    for cp in cartproducts:
        curr_product = Product.objects.filter(id=cp.product_id).get()
        products.append(curr_product)
        quantities_per_name[curr_product.name] = cp.quantity
    return products, quantities_per_name


def convert_cartproduct_to_orderproduct(cartproducts_queryset):
    cartproducts = list(cartproducts_queryset)
    for each_cp in cartproducts:
        new_orderproduct = OrderProduct(user=UserModel.filter(pk=each_cp.user_id))
        new_orderproduct.save()


def get_popular_items():
    products = Product.objects.all().order_by()
    popular_products = products.order_by('-sold')[:3]
    return popular_products