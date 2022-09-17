from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.success(request, 'Произошла ошибка авторизации, убедитесь в корректном вводе информации')
            return redirect('user_login')
    else:
        return render(request, 'auth/login.html', {})


def signup(request):
    form = RegUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'auth/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'Вы успешно вышли из системы')
    return redirect('home')


def complete_reg(request):
    if request.method == 'POST':
        form = UserOptionalForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            messages.success(request, 'Вы успешно обновили информацию профиля')
            return redirect('profile')
        else:
            messages.success(request, 'Произошла ошибка ввода, проверьте корректность введенной информации')
    else:
        form = UserOptionalForm()
    return render(request, 'auth/complete_reg.html', {'form': form})


def redact(request):
    user_optional_info = UserOptional.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = UserOptionalForm(request.POST, instance=user_optional_info)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            messages.success(request, 'Вы успешно обновили информацию профиля')
            return redirect('home')
        else:
            messages.success(request, 'Произошла ошибка ввода, проверьте корректность введенной информации')
            return redirect('redact')
    else:
        form = UserOptionalForm(instance=user_optional_info)
    return render(request, 'auth/redact.html', {'form': form})


def profile(request):
    user_info = UserOptional.objects.filter(user_id=request.user.id).first()
    return render(request, 'auth/profile.html', {'user_info': user_info})
