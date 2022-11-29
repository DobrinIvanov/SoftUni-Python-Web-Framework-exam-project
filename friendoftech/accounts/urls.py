from django.urls import path

from friendoftech.accounts.views import SignUpView, SignOutView, SignInView, ProfileView, ProfileEditView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/profile-details/', ProfileView.as_view(), name='profile-details'),
    path('<int:pk>/profile-edit/', ProfileEditView.as_view(), name='profile-edit'),
)
