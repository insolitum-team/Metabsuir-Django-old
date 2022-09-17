from django.shortcuts import render
from .models import *


def home(request):
    sections = Section.objects.all()
    themes = Theme.objects.all()
    side_menu_items = SideMenuItem.objects.all()
    return render(request, "app/index.html", {
        'sections': sections,
        'themes': themes,
        'side_menu_items': side_menu_items
    })


def theme(request, theme_id):
    current_theme = Theme.objects.get(pk=theme_id)
    comments = Message.objects.filter(theme_id=theme_id)
    return render(request, 'app/current_theme.html', {'theme': current_theme, 'messages': comments})
