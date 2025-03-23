from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from account.models import UserProfile
from django.contrib.auth import logout

@login_required
def account(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)  
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=user)

    context = {
        'first_name' : user_profile.first_name,
        'last_name' : user_profile.last_name,
        'middle_name' : user_profile.middle_name,
        'role' : user_profile.role,
        'workplace' : user_profile.workplace,
        'email' : user_profile.email,
        'phone' : user_profile.phone,
    }

    return render(request, 'account/account.html', context)

def index(request):
    return "Прив"

def logout_out(request):
    request.session.flush() 
    logout(request)
    return redirect('login')

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        user_profile = UserProfile.objects.get(user=user)

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.save()

        user_profile.first_name = request.POST.get('first_name')
        user_profile.last_name = request.POST.get('last_name')
        user_profile.middle_name = request.POST.get('middle_name')
        user_profile.workplace = request.POST.get('workplace')
        user_profile.phone = request.POST.get('phone')
        user_profile.email = request.POST.get('email')
        user_profile.save()

        messages.success(request, 'Данные успешно обновлены!')
        return redirect('account')

    return redirect('account')