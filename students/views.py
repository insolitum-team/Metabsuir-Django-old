from django.shortcuts import render


def user_login(request):
    return render(request, 'auth/login.html', {})


def signup(request):
    return render(request, 'auth/signup.html', {})
