from django.shortcuts import render
from .models import *


def home(request):
    sections = Section.objects.all()
    themes = Theme.objects.all()
    return render(request, "app/index.html", {'sections': sections, 'themes': themes})


def theme_by_section(request, section_id):
    themes = Theme.objects.filter(section_id=section_id).all()
    return render(request, 'app/themes_by_section.html', {'themes': themes})
