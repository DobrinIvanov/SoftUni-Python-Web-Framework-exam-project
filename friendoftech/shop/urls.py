from django.urls import path, include

from friendoftech.shop import views as shop_views

urlpatterns = (
    path('products/', include([
        path('', shop_views.ProductListView.as_view(), name='product-list'),
        path('<int:pk>/', shop_views.ProductDetailsView.as_view(), name='product-details'),
    ])),
    path('add-to-cart/<int:product_pk>/<int:user_pk>/', shop_views.add_to_cart, name='add_to_cart'),
)
