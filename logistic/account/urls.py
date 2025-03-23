from django.urls import path
from account import views

urlpatterns = [
    path('', views.account, name='account'), 
    path('update_profile/', views.update_profile, name='update_profile'),
    path('logout_out/', views.logout_out, name='logout_out'),
]