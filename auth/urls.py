from django.urls import path
from .views import *

urlpatterns = [
    path("login", user_login, name="user_login"),
    path("signup", signup, name="signup"),
]
