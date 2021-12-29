from rest_framework import serializers
from .models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    """Сериализатор для пиццы"""
    class Meta:
        model = Pizza
        fields = ['pk', 'name', 'topping', 'diameter']
