from django.contrib import admin

from friendoftech.accounts.models import AppUser


# Register your models here.
# admin.site.register(User)


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    fields = (
        'first_name', 'last_name',
        'email', 'password',
        'is_staff', 'is_superuser',
        'groups', 'user_permissions',
        'last_login',
        )
