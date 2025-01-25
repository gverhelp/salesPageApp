"""
URL configuration for salesPage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from salesPage.views import home, article_list, article_detail

urlpatterns = [
    path('', home, name='home'),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)