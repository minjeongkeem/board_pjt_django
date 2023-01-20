from django import forms
from .models import Comment, Article

class Articleform(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    content = forms.CharField(min_length=30, max_length=300)
    class Meta:
        model = Article
        fields = ('name', 'content', )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
