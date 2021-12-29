from django.views import generic

from .models import Pizza


class IndexView(generic.ListView):
    """
    Представление master
    """
    template_name = 'Pizza/index.html'
    context_object_name = 'pizza_list'

    def get_queryset(self):
        """
        Возвращает список из трёх пицц
        """
        return Pizza.objects.order_by('-name')[:3]


class DetailView(generic.DetailView):
    """
    Представление detail
    """
    model = Pizza
    template_name = 'Pizza/detail.html'
