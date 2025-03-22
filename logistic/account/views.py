from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def account(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        # Аутентификация пользователя
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Перенаправляем на главную страницу
        else:
            messages.error(request, 'Неверный email или пароль')
    
    return render(request, 'register/login.html')
