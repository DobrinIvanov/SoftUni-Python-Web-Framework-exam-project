from django.urls import path, include

from friendoftech.shop import views as shop_views

urlpatterns = (
    path('products/', include([
        path('', shop_views.ProductListView.as_view(), name='list_products'),
        path('edit/<int:pk>/', shop_views.EditProductView.as_view(), name='edit_product'),
    ])),
)
