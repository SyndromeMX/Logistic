from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_in(request):
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

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Проверка совпадения паролей
        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        # Проверка, существует ли пользователь с таким email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует')
            return redirect('register')

        # Создание нового пользователя
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Аутентификация и вход пользователя после регистрации
        login(request, user)
        messages.success(request, 'Регистрация прошла успешно! Добро пожаловать.')
        return redirect('index')  # Перенаправляем на главную страницу
    
    return render(request, 'register/register.html')