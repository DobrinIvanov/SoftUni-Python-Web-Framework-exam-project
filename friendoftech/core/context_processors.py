from friendoftech.shop.functions import get_total_items_per_user_cart


def access_cart_items_count(request):
    cart_items_count = get_total_items_per_user_cart(request.user.pk)
    return {'cart_items': cart_items_count}
