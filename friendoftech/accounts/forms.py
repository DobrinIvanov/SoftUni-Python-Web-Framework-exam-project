from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms as django_forms

from friendoftech.accounts.models import Profile

UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):

    first_name = django_forms.CharField()
    last_name = django_forms.CharField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name')

    def save(self, commit=True):

        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )

        if commit:
            profile.save()

        return user
