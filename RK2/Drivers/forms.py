from .models import Driver, Carstation
from django.forms import ModelForm, TextInput, NumberInput, Select


class DriverCreateFrom(ModelForm):
    """Форма для добавления водителя"""
    class Meta:
        model = Driver
        fields = ['second_name', 'first_name', 'salary', 'carstation_id']
        widgets = {
            'second_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите фамилию'}),
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя'}),
            'salary': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите зарплату'}),
            'carstation_id': Select(attrs={'class': 'form-select'})
        }


class DriverUpdateForm(ModelForm):
    """Форма для редактирования водителя"""
    class Meta:
        model = Driver
        fields = ['salary', 'carstation_id']
        widgets = {
            'salary': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите зарплату'}),
            'carstation_id': Select(attrs={'class': 'form-select'})
        }


class CarstationCreateForm(ModelForm):
    """Форма для добавления автопарка"""
    class Meta:
        model = Carstation
        fields = ['name', 'adress']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'})
        }


class CarstationUpdateForm(ModelForm):
    """Форма для изменения автопарка"""
    class Meta:
        model = Carstation
        fields = ['adress']
        widgets = {
            'adress': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите адрес'})
        }
