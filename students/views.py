from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('user_login')
    else:
        return render(request, 'auth/login.html', {})


def signup(request):
    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        form = RegUserForm()
        return render(request, 'auth/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')
