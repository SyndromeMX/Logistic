from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.models import UserProfile

@login_required
def account(request):
    # Получаем данные текущего пользователя
    user = request.user

    # Получаем профиль пользователя через связанный объект
    try:
        user_profile = UserProfile.objects.get(user=user)  # Ищем профиль по связанному пользователю
    except UserProfile.DoesNotExist:
        # Если профиль не найден, создаем его (опционально)
        user_profile = UserProfile.objects.create(user=user)

    # Создаем контекст для передачи данных в шаблон
    context = {
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'phone': user_profile.phone,  # Данные из UserProfile
        'role': user_profile.role,   # Данные из UserProfile
        # Добавьте другие поля, если они есть в вашей модели UserProfile
    }

    # Рендерим шаблон с передачей контекста
    return render(request, 'account/account.html', context)

def index(request):
    return "Прив"

def logout(request):
    return "Прив"