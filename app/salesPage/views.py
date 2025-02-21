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
    articles = Article.objects.all()
    orders = Order.objects.all()
    
    return render(request, "admin/admin_dashboard.html", {'articles': articles, 'orders': orders})


@login_required(login_url='/admin-login/')
@user_passes_test(admin_required, login_url='/admin-login/')
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        files = request.FILES.getlist('images')

        if form.is_valid():
            article = form.save()
            for file in files:
                ArticleImage.objects.create(article=article, image=file)
            return redirect('admin_dashboard')
    else:
        form = ArticleForm()
    return render(request, 'admin/add_article.html', {'form': form})


@login_required(login_url='/admin-login/')
@user_passes_test(admin_required, login_url='/admin-login/')
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    images = article.images.all()

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        files = request.FILES.getlist('images')

        if form.is_valid():
            form.save()
            for file in files:
                ArticleImage.objects.create(article=article, image=file)
            return redirect('admin_dashboard')

    else:
        form = ArticleForm(instance=article)

    return render(request, 'admin/edit_article.html', {'form': form, 'article': article, 'images': images})


@login_required(login_url='/admin-login/')
@user_passes_test(admin_required, login_url='/admin-login/')
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('admin_dashboard')


@login_required(login_url='/admin-login/')
@user_passes_test(admin_required, login_url='/admin-login/')
def delete_image(request, image_id):
    image = get_object_or_404(ArticleImage, id=image_id)
    article_id = image.article.id  # On récupère l'ID de l'article associé
    image.delete()  # Suppression de l'image
    return redirect('edit_article', article_id=article_id) 