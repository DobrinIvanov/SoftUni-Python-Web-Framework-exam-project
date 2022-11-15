from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from friendoftech.accounts.manager import MyUserManager
from django.db import models

# Create your models here.


# class MyUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(
#         unique=True,
#         blank=False,
#         null=False,
#     )
#
#     date_joined=models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     is_staff = models.BooleanField(
#         default=False,
#         null=False,
#         blank=False,
#     )
#
#     objects = MyUserManager()


# class Profile(models.Model):
#     user = models.OneToOneField(
#         MyUser,
#         primary_key=True,
#         on_delete=models.CASCADE,
#     )
#
#     first_name = models.CharField(
#         max_length=30,
#     )
#
#     last_name = models.CharField(
#         max_length=30,
#     )
