from django.urls import path, include
from friendoftech.core.views import IndexView, ContactUsView, NewsView, AboutUsView, ArticleView, search_results

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('news/', include([
        path('', NewsView.as_view(), name='news'),
        path('<int:articleid>/details/', ArticleView.as_view(), name='article-details'),
    ])),
    path('about/', AboutUsView.as_view(), name='about'),
    path('search-results/', search_results, name='search-results'),

)
