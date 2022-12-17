from friendoftech.core.models import Article


def get_latest_articles():
    articles = Article.objects.all()
    latest_articles = articles.order_by('created')[:3]
    return latest_articles
