from django.urls import path
from .views import *


urlpatterns = [
    path('theme/<section_id>', add_theme, name='add_theme'),
]
