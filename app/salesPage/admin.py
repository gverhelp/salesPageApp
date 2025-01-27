from django.contrib import admin
from .models import Article, ArticleImage

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    
class ArticleImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'image')
    list_display_links = ('id', 'article')

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleImage, ArticleImageAdmin)
