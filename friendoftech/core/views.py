# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from friendoftech.core.forms import ContactForm
from django.core.mail import send_mail


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
    pass


class AboutUsView(views.TemplateView):
    pass

    # def form_valid(self, form_class):
    #     form_class.send_mail()
    #     return super().form_valid(form=form_class)
