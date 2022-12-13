from django.urls import path, include

from friendoftech.shop import views as shop_views

urlpatterns = (
    path('products/', include([
        path('', shop_views.ProductListView.as_view(), name='product-list'),
        path('<int:pk>/details/', shop_views.ProductDetailsView.as_view(), name='product-details'),
    ])),
    # with usr pk
    path('<int:pk>/', include([
        path('cart/', shop_views.CartView.as_view(), name='cart'),
        path('checkout/', shop_views.CheckoutView.as_view(), name='checkout'),
        path('<int:product_pk>/add-to-cart/', shop_views.add_to_cart, name='add-to-cart'),
        path('<int:pid>/', include([
            path('remove-cart-product/', shop_views.remove_cartproduct_view, name='remove-cart-product'),
            path('add-cart-product/', shop_views.add_cartproduct_view, name='add-cart-product'),
        ])),
        path('<int:orderid>/', include([
            path('edit-order/', shop_views.edit_order_cart_redirect, name='edit-order-cart-redirect'),
            path('complete-order/', shop_views.CompleteOrderView.as_view(), name='complete-order'),
        ])),
    ])),
)
