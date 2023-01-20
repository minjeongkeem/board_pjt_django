from django import forms
from .models import Content, Person

class ContentForm(forms.ModelForm):
    content = forms.CharField(min_length=30, max_length=300)
    class Meta:
        model = Content
        fields = ('content',)

