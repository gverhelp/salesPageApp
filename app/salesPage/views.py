from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, ArticleImage
from .forms import ArticleForm

# Create your views here.
def home(request):
    return render(request, 'base.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_delete(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    
    return render(request, 'articles/article_delete.html', {'article': article})


def article_update(request, article_id):
    
    article = get_object_or_404(Article, id=article_id)
    # images = article.images.all()
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        
        files = request.FILES.getlist('image')
        
        if form.is_valid():
            form.save()
            
            for file in files:
                ArticleImage.objects.create(article=article, image=file)
                
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'articles/article_update.html', {'form': form, 'article': article})


def article_create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)

        files = request.FILES.getlist('image')

        if article_form.is_valid():
            article = article_form.save()

            for file in files:
                ArticleImage.objects.create(article=article, image=file)

            return redirect('article_list')  # Rediriger vers la liste des articles

    else:
        article_form = ArticleForm()

    return render(request, 'articles/article_create.html', {'article_form': article_form})
