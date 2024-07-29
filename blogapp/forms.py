from django import forms
from tinymce.widgets import TinyMCE
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'featured']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }
