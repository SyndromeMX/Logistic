from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    ROLE_CHOICES = [
        ('admin', 'Администратор'),
        ('manager', 'Менеджер'),
        ('employee', 'Сотрудник'),
        ('client', 'Клиент'),
    ]
    
    first_name = models.CharField(max_length=50, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', blank=True, null=True)
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон', unique=True, blank=True, null=True)
    email = models.EmailField(verbose_name='Email', unique=True, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name='Роль', default='client')
    workplace = models.CharField(max_length=100, verbose_name='Место работы', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Дата создания аккаунта', default=timezone.now)

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.role})"

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'