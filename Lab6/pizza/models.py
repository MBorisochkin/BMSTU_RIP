from django.db import models


class Pizza(models.Model):
    """Модель Пицца"""
    # Список кортежей для атрибута choices поля diameter
    PIZZA_DIAMETER = [(23, '23 cм'), (30, '30 cм'), (35, '35 cм'), (40, '40 cм')]
    name = models.CharField(max_length=100)
    topping = models.CharField(max_length=200, blank=True, null=True)
    diameter = models.IntegerField(blank=True, null=True, choices=PIZZA_DIAMETER)

    class Meta:
        managed = False
        db_table = 'pizza'
