from django.urls import path
from cargo import views

urlpatterns = [
    path('', views.cargo,name='cargo'),
    path('create_cargo/', views.create_cargo, name='create_cargo'), 
    path('delete_cargo/', views.delete_cargo, name='delete_cargo'),
    path('filter_cargo/', views.filter_cargo, name='filter_cargo'),
]