from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.
def home(request):
    return render(request, 'base.html')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})