from django.urls import path

from friendoftech.accounts.views import RegisterUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
)
