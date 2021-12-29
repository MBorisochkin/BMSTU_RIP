from django.db import models
from django.urls import reverse


class Carstation(models.Model):
    """Модель Автопарк"""
    name = models.CharField(max_length=50, verbose_name='Название')
    adress = models.CharField(max_length=150, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Автопарк'
        verbose_name_plural = 'Автопарки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Drivers:carstations')


class Driver(models.Model):
    """Модель Водитель"""
    second_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    salary = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Заработная плата')
    carstation_id = models.ForeignKey(Carstation, null=True, on_delete=models.SET_NULL, verbose_name='Автопарк')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return self.second_name + " " + self.first_name

    def get_absolute_url(self):
        return reverse('Drivers:driver_detail', args=[str(self.id)])
