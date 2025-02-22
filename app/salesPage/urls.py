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
from salesPage.views import article_list, article_detail, contact_me, admin_login, admin_dashboard, admin_logout, edit_article, delete_article, add_article, delete_image, delete_order

urlpatterns = [
    path('', article_list),
    path('articles/', article_list, name='article_list'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
    path('me-contacter/', contact_me, name='contact_me'),
    
    path('admin-login/', admin_login, name='admin_login'),
    path('admin-logout/', admin_logout, name='admin_logout'),
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    
    path('add-article/', add_article, name='add_article'),
    path('edit-article/<int:article_id>/', edit_article, name='edit_article'),
    path('delete-article/<int:article_id>/', delete_article, name='delete_article'),
    path('delete-image/<int:image_id>/', delete_image, name='delete_image'),
    path('delete-order/<int:order_id>/', delete_order, name='delete_order'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)