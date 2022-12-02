from django.contrib.auth import views as auth_views
from django.urls import path, include

from friendoftech.accounts.views import SignUpView, SignOutView, SignInView, ProfileView, ProfileEditView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('<int:pk>/', include([
        path('profile-details/', ProfileView.as_view(), name='profile-details'),
        path('profile-edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('password/', auth_views.PasswordChangeView.as_view(), name='change-password'),
    ])),
    path('<int:pk>/profile-details/', ProfileView.as_view(), name='profile-details'),
    path('<int:pk>/profile-edit/', ProfileEditView.as_view(), name='profile-edit'),
)
