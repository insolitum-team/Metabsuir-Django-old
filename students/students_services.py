from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def form_signup(request, form):
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return True
