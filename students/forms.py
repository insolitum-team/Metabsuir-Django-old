from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *
from django.forms import ModelForm


class UserOptionalForm(ModelForm):
    class Meta:
        model = UserOptional
        fields = ('faculty', 'specialty', 'group', 'description', 'tg_link')
        labels = {
            'faculty': 'Факультет',
            'specialty': 'Специальность',
            'group': 'Группа',
            'description': 'Описание',
            'tg_link': 'Ссылка на телеграм',
        }
        widgets = {
            'faculty': forms.Select(
                attrs={'class': 'form-control'},
                choices=[
                    ('ИЭФ', 'ИЭФ'),
                    ('ФКП', 'ФКП'),
                    ('ФИТУ', 'ФИТУ'),
                    ('ФРЭ', 'ФРЭ'),
                    ('КСиС', 'КСиС'),
                    ('ВФ', 'ВФ'),
                ]
            ),
            'specialty': forms.Select(
                attrs={'class': 'form-control'},
                choices=[
                    ('ЭЭБ', 'ЭЭБ'),
                    ('ЭМ', 'ЭМ'),
                    ('ИСиТ(Л)', 'ИСиТ(Л)'),
                    ('ИСиТ(Э)', 'ИСиТ(Э)'),
                    ('ИСиТ(Б)', 'ИСиТ(Б)'),
                    ('ЭСБ', 'ЭСБ'),
                ]
            ),
            'group': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'tg_link': forms.URLInput(attrs={'class': 'form-control'}),
        }


class RegUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
