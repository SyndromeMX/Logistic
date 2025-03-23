from django.db import models

class Company(models.Model):
    # Название компании
    name = models.CharField(max_length=255, verbose_name="Название компании")

    # Номер телефона
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")

    # Город базирования
    city = models.CharField(max_length=100, verbose_name="Город базирования")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"