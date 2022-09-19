from django.shortcuts import render, redirect
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
    return render(request, 'app/current_theme.html', {'theme': current_theme, 'comments': comments})


def send_reply_to_message(request, theme_id, user_id):
    content = request.POST['content']
    Message.objects.create(
        content=content,
        theme=theme_id,
        reply_to=user_id,
        sender=request.user,
    )
    return redirect('theme', theme_id)


def send_reply_to_theme(request, theme_id):
    content = request.POST['content']
    Message.objects.create(
        content=content,
        theme=theme_id,
        reply_to=None,
        sender=request.user,
    )

