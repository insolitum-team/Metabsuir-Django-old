from django.urls import path
from .views import *

urlpatterns = [
    path("login", user_login, name="user_login"),
    path("signup", signup, name="signup"),
    path("logout", logout_user, name="logout_user"),
    path("complete", complete_reg, name="complete_reg"),
    path("redact", redact, name="redact"),
    path('profile', profile, name='profile')
]
