from django.urls import path
from friendoftech.core.views import IndexView, ContactUsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactUsView.as_view(), name='contact')
)