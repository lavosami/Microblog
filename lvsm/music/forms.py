from django import forms
from .models import *


class NewPostForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(max_length=255, label="URL", widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    photo = forms.ImageField(allow_empty_file=True, required=False)
    is_published = forms.BooleanField(required=False, initial=True)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="No genre")
