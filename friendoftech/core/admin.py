from django.contrib import admin

from friendoftech.core.models import Article, ClientMessage


# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(ClientMessage)
class ClientMessageAdmin(admin.ModelAdmin):

    list_display = [
        'full_name',
        'subject',
    ]
    search_fields = ("sent_on", )


admin.site.site_header = 'Friend of Tech Dashboard'
