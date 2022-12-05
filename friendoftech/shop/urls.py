from django.urls import path, include

from friendoftech.shop import views as shop_views

urlpatterns = (
    path('products/', include([
        path('', shop_views.ProductListView.as_view(), name='product-list'),
        path('<int:pk>/', include([
            path('edit/', shop_views.ProductEditView.as_view(), name='product-edit'),
            path('details/', shop_views.ProductDetailsView.as_view(), name='product-details')
        ])),
    ])),
)
