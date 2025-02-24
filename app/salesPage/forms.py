from django import forms
from .models import Article, ArticleImage

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'price']

