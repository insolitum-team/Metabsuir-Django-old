from django.shortcuts import render
from .models import *


def home(request):
    sections = Section.objects.all()
    themes = Theme.objects.all()
    return render(request, "app/index.html", {'sections': sections, 'themes': themes})


def theme(request, theme_id):
    current_theme = Theme.objects.get(pk=theme_id)
    messages = Message.objects.filter(theme_id=theme_id)
    return render(request, 'app/current_theme.html', {'theme': current_theme, 'messages': messages})
