from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from account.models import UserProfile 

def login_in(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('account') 
        else:
            messages.error(request, 'Неверный email или пароль')
    
    return render(request, 'register/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)

        UserProfile.objects.create(user=user)

        login(request, user)
        messages.success(request, 'Регистрация прошла успешно! Добро пожаловать.')
        return redirect('login')
    
    return render(request, 'register/register.html')