from django.db import models


class Pizza(models.Model):
    """Модель Пицца"""
    name = models.CharField(max_length=100, verbose_name='Название')
    photo = models.ImageField(verbose_name='Изображение')
    topping = models.CharField(max_length=200, verbose_name='Состав')
    diameter = models.IntegerField(default=23, verbose_name='Диаметр пиццы в см')

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'

    def __str__(self):
        return self.name
