from django.shortcuts import render
from .forms import *


def add_theme(request, section_id):
    section = Section.objects.get(pk=section_id)
    form = AddTheme(request.POST or None)
    if form.is_valid():
        new_theme = form.save(commit=False)
        new_theme.section = section
        new_theme.author = request.user
        new_theme.save()
    return render(request, 'poster/add_theme.html', {'form': form})
