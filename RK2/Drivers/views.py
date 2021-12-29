from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import Driver, Carstation
from .forms import DriverCreateFrom, DriverUpdateForm, CarstationCreateForm, CarstationUpdateForm


def index(request):
    return render(request, 'Drivers/index.html')


class DriverListView(generic.ListView):
    """Список водителей"""
    template_name = 'Drivers/Driver/List.html'
    context_object_name = 'driver_list'

    def get_queryset(self):
        return Driver.objects.order_by('second_name', 'first_name')


class DriverDetailView(generic.DetailView):
    """Информация о конкретном водителе"""
    model = Driver
    template_name = 'Drivers/Driver/Detail.html'


class DriverCreateView(generic.CreateView):
    """Добавление водителя"""
    model = Driver
    template_name = 'Drivers/Driver/Create.html'
    form_class = DriverCreateFrom


class DriverUpdateView(generic.UpdateView):
    """Изменение водителя"""
    model = Driver
    template_name = 'Drivers/Driver/Update.html'
    form_class = DriverUpdateForm


class DriverDeleteView(generic.DeleteView):
    """Удаление водителя"""
    model = Driver
    template_name = 'Drivers/Driver/Delete.html'
    success_url = reverse_lazy('Drivers:drivers')


class CarstationListView(generic.ListView):
    """Список автопарков"""
    template_name = 'Drivers/Carstation/List.html'
    context_object_name = 'carstation_list'

    def get_queryset(self):
        return Carstation.objects.order_by('name')


class CarstationCreateView(generic.CreateView):
    """Добавление автопарка"""
    model = Carstation
    template_name = 'Drivers/Carstation/Create.html'
    form_class = CarstationCreateForm


class CarstationUpdateView(generic.UpdateView):
    """Изменение автопарка"""
    model = Carstation
    template_name = 'Drivers/Carstation/Update.html'
    form_class = CarstationUpdateForm


class CarstationDeleteView(generic.DeleteView):
    """Удаление автопарка"""
    model = Carstation
    template_name = 'Drivers/Carstation/Delete.html'
    success_url = reverse_lazy('Drivers:carstations')


def report(request):
    top_drivers = Driver.objects.select_related('carstation_id').filter(salary__gte=50000)\
        .order_by('-salary', 'second_name', 'first_name')
    return render(request, 'Drivers/report.html', {'top_drivers': top_drivers})
