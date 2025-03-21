from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Пример маршрута для главной страницы
    path('about/', views.about, name='about')
]