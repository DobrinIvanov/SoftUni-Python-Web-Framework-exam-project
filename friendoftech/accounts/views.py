# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
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

    # def form_valid(self, form):
    #     """If the form is valid, save the associated model."""
    #     self.object = form.save()
    #     return super().form_valid(form)


class SignInView(auth_views.LoginView):
    template_name = 'accounts/sign-in.html'

    def get_success_url(self):
        return reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class SignOutView(auth_views.LogoutView, LoginRequiredMixin):
    template_name = 'accounts/sign-out.html'
    success_url = reverse_lazy('index')


class ProfileDetailsView(views.DetailView, LoginRequiredMixin):
    model = UserModel
    template_name = 'accounts/profile-details.html'

    # def get_object(self, queryset=None):
    #     return UserModel.objects.filter(id=self.request.user.pk).get()
    # # raise_exception = False


class ProfileEditView(views.UpdateView, LoginRequiredMixin):
    model = UserModel
    template_name = 'accounts/profile-edit.html'
    fields = ('first_name', 'last_name', 'email')

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.kwargs['pk']})

    def dispatch(self, request, *args, **kwargs):
        result = super().dispatch(*args, **kwargs)
        return result


class ChangePasswordView(auth_views.PasswordChangeView, LoginRequiredMixin):
    form_class = PasswordChangeForm
    template_name = 'accounts/profile-password-update.html'
    success_url = reverse_lazy('index')


