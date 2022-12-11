# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from friendoftech.core.forms import ContactForm
from django.core.mail import send_mail

from friendoftech.core.models import Article


# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        # TODO Recommended Items
        context_data['recommended_products'] = ...


class ContactUsView(views.FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')


class NewsView(views.ListView):
    model = Article
    template_name = 'core/news.html'


class AboutUsView(views.TemplateView):
    template_name = 'core/about.html'
