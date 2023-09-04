from django.shortcuts import render
#from django.http import HttpResponse
from .models import Article
from django.utils.translation import gettext as _

global_context = {
    'author_name': _('Алексей Стогов'),
}



def home_page(request):
    articles = Article.objects.all()
    context = global_context | {'articles': articles}
    return render(request, 'home_page.html', context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = global_context | {'article': article}
    return render(request, 'article_page.html', context)