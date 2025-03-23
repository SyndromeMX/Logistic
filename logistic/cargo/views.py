from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from cargo.models import Cargo

def cargo(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)  
    user_company = user_profile.workplace

    # Фильтруем грузы по компании пользователя
    cargo_list = Cargo.objects.filter(company=user_company)
    content = {
        'workplace' : user_profile.workplace,
        'cargo_list': cargo_list,
    }
    
    return render(request, 'cargo/cargo.html', content)

def create_cargo(request):
    pass

def delete_cargo():
    pass
def update_cargo():
    pass
def filter_cargo():
    pass

