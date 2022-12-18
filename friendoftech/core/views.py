# from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from friendoftech.core.forms import ContactForm

from friendoftech.core.functions import get_latest_articles
from friendoftech.core.models import Article
from friendoftech.shop.functions import get_popular_products
from friendoftech.shop.models import Product
from django.db.models import Q

UserModel = get_user_model()
# Create your views here.


class IndexView(views.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        popular_products = get_popular_products()
        latest_articles = get_latest_articles()

        context_data['popular_products'] = popular_products
        context_data['latest_articles'] = latest_articles
        return context_data


class ContactUsView(views.CreateView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')


class NewsView(views.ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'core/news.html'
    paginate_by = 6


class ArticleView(views.DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'core/article.html'


class AboutUsView(views.TemplateView):
    template_name = 'core/about.html'


def search_results(request):

    context = {}

    if request.method == 'POST':

        search_string = request.POST.get('searched')
        search_result = list(Product.objects.filter(
            Q(name__icontains=search_string) | Q(description__icontains=search_string)
        ))
        search_result.append(
            Article.objects.filter(
                Q(title__icontains=search_string) | Q(content__icontains=search_string)
            )
        )
        context = {
            'search_string': search_string,
            'search_result': search_result[:-1],
        }
        return render(request, 'core/search-results.html', context)
    else:
        return render(request, 'core/search-results.html', context)


