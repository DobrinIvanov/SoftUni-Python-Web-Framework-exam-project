from django.contrib.auth import models as auth_models
from friendoftech.accounts.managers import AppUserManager
from django.db import models


# Create your models here.

# UserModel = get_user_model()
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    MAX_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    # TODO
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email



