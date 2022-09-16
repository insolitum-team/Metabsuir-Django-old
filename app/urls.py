from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('current-theme/<theme_id>', theme, name='theme'),
]
