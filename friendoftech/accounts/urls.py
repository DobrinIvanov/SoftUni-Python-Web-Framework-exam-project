from django.urls import path, include
from friendoftech.accounts.views import SignUpView, SignOutView, SignInView, ProfileDetailsView, ProfileEditView, \
    ChangePasswordView

urlpatterns = (
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('password/', ChangePasswordView.as_view(), name='change-password'),
    path('<int:pk>/', include([
        path('profile-details/', ProfileDetailsView.as_view(), name='profile-details'),
        path('profile-edit/', ProfileEditView.as_view(), name='profile-edit'),
    ])),
)
