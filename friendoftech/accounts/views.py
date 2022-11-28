# from django.shortcuts import render

from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views, login, get_user_model
from django.views import generic as views
from friendoftech.accounts.forms import AppUserCreationForm


UserModel = get_user_model()
# Create your views here.


class SignUpView(views.CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/sign-up.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'accounts/sign-out.html'
    success_url = reverse_lazy('index')


class ProfileView(views.DetailView):
    model = UserModel
    template_name = 'accounts/profile-details.html'
    context_object_name = 'user'


