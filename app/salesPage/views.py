from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Article, ArticleImage, Order
from .forms import ArticleForm

# Create your views here.
def contact_me(request):
    return render(request, 'contact/contact_me.html')


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    articles = Article.objects.all()
    prev_article = Article.objects.filter(id__lt=article.id).order_by('-id').first()
    next_article = Article.objects.filter(id__gt=article.id).order_by('id').first()
    
    if request.method == 'POST':
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        article_title = request.POST.get('article')

        selected_article = Article.objects.filter(title=article_title).first()
    
        if (email or number) and selected_article:
            Order.objects.create(
                email=email,
                phone_number=number,
                message=message,
                article=selected_article
            )
            return redirect('article_detail', article_id=article.id)

    return render(request, 'articles/article_detail.html', {
        'actual_article': article,
        'articles': articles,
        'prev_article': prev_article,
        'next_article': next_article,
    })


def admin_required(user):
    return user.is_authenticated and user.is_superuser


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('/admin-dashboard/')
        else:
            messages.error(request, "Identifiants incorrects ou accès non autorisé.")

    return render(request, 'admin/admin_login.html')


def admin_logout(request):
    logout(request)
    return redirect("/admin-login/")


@login_required(login_url='/admin-login/')
@user_passes_test(admin_required, login_url='/admin-login/')
def admin_dashboard(request):
    return render(request, "admin/admin_dashboard.html")


# def article_delete(request, article_id):
    
#     article = get_object_or_404(Article, id=article_id)
    
#     if request.method == 'POST':
#         article.delete()
#         return redirect('article_list')
    
#     return render(request, 'articles/article_delete.html', {'article': article})


# def article_update(request, article_id):
    
#     article = get_object_or_404(Article, id=article_id)
#     # images = article.images.all()
    
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES, instance=article)
        
#         files = request.FILES.getlist('image')
        
#         if form.is_valid():
#             form.save()
            
#             for file in files:
#                 ArticleImage.objects.create(article=article, image=file)
                
#             return redirect('article_detail', article_id=article.id)
#     else:
#         form = ArticleForm(instance=article)

#     return render(request, 'articles/article_update.html', {'form': form, 'article': article})


# def article_create(request):
#     if request.method == 'POST':
#         article_form = ArticleForm(request.POST)

#         files = request.FILES.getlist('image')

#         if article_form.is_valid():
#             article = article_form.save()

#             for file in files:
#                 ArticleImage.objects.create(article=article, image=file)

#             return redirect('article_list')  # Rediriger vers la liste des articles

#     else:
#         article_form = ArticleForm()

#     return render(request, 'articles/article_create.html', {'article_form': article_form})
