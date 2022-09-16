from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('themes/<section_id>', theme_by_section, name='theme_by_section'),
]
