# from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views import generic as views


# Create your views here.

class RegistrationView(views.FormView):
    form_class = UserCreationForm()
    template_name = 'accounts/registration.html'
