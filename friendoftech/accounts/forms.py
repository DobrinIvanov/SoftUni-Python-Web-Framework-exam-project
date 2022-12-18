from django.contrib.auth import forms as auth_forms, get_user_model
from django import forms as django_forms

UserModel = get_user_model()


class AppUserCreationForm(auth_forms.UserCreationForm):

    first_name = django_forms.CharField()
    last_name = django_forms.CharField()

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name')
        widgets = {
            UserModel.USERNAME_FIELD: django_forms.TextInput(attrs={'placeholder': 'Email'}),
            # 'password1': django_forms.HiddenInput
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = django_forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = django_forms.PasswordInput(attrs={'placeholder': 'Confirm password'})
        self.fields['first_name'].widget = django_forms.TextInput(attrs={'placeholder': 'First Name'})
        self.fields['last_name'].widget = django_forms.TextInput(attrs={'placeholder': 'Last Name'})

    # def save(self, commit=True):
    #     super().save(commit=commit)
