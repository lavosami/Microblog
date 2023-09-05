from django import forms
from django.core.exceptions import ValidationError

from .models import *


class NewPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['genre'].empty_label = "No genre selected"

    class Meta:
        model = Music
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("The length of title is not available")
        return title
