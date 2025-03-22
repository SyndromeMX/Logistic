from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),  # Пример маршрута для страницы регистрации
    path('login/', views.login_in,name='login')
]