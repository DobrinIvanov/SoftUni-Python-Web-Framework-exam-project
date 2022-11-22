from django.urls import path
from friendoftech.core.views import IndexView, ContactUsView, NewsView, AboutUsView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('news/', NewsView.as_view(), name='news'),
    path('about/', AboutUsView.as_view(), name='about'),
)
