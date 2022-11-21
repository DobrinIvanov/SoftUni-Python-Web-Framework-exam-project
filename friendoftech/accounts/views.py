# from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic as views
from friendoftech.accounts.forms import AppUserCreationForm


# Create your views here.

class RegisterUserView(views.CreateView):
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')


