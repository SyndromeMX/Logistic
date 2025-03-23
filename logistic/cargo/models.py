from django.db import models

class Cargo(models.Model):
    # Поля для массы и габаритов
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Масса (кг)")
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Длина (м)")
    width = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ширина (м)")
    height = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Высота (м)")

    departure_point = models.CharField(max_length=255, verbose_name="Точка отправления")
    destination_point = models.CharField(max_length=255, verbose_name="Точка прибытия")

    departure_date = models.DateTimeField(verbose_name="Дата отправления")
    arrival_date = models.DateTimeField(verbose_name="Дата прибытия")

    company = models.CharField(max_length=255, verbose_name="Компания")

    def __str__(self):
        return f"Груз из {self.departure_point} в {self.destination_point}"

    class Meta:
        verbose_name = "Груз"
        verbose_name_plural = "Грузы"