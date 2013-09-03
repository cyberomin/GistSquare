from django import forms
from models import Article
from models import Comments

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','body')

"""
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body')
"""