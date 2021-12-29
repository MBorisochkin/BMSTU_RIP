from django.shortcuts import render
from django.views import generic

from .models import Pizza, Pasta


def index(request):
    return render(request, 'pizzapasta/index.html')


class PizzaIndexView(generic.ListView):
    """
    Представление master для пиццы
    """
    template_name = 'pizzapasta/pizza/main.html'
    context_object_name = 'pizza_list'

    def get_queryset(self):
        """
        Возвращает список пицц
        """
        return Pizza.objects.order_by('name')


class PizzaDetailView(generic.DetailView):
    """
    Представление detail для пиццы
    """
    model = Pizza
    template_name = 'pizzapasta/pizza/detail.html'


class PastaIndexView(generic.ListView):
    """
    Представление master для пасты
    """
    template_name = 'pizzapasta/pasta/main.html'
    context_object_name = 'pasta_list'

    def get_queryset(self):
        """
        Возвращает список паст
        """
        return Pasta.objects.order_by('name')


class PastaDetailView(generic.DetailView):
    """
    Представление detail для пасты
    """
    model = Pasta
    template_name = 'pizzapasta/pasta/detail.html'
