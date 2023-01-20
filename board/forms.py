from django import forms
from .models import Comment, Article

class Article(forms.ModelForm):

    content = forms.CharField(min_length=30, max_length=300)
    class Meta:
        model = Article
        fields = ('name', 'content', )


class PersonForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
