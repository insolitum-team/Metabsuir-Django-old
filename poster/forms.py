from django.forms import ModelForm
from django import forms
from app.models import *


class AddTheme(ModelForm):
    class Meta:
        model = Theme
        fields = ('name', 'main_post')
        labels = {
            'name': 'Название',
            'main_post': 'Главный пост',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'main_post': forms.Textarea(attrs={'class': 'form-control'}),
        }
