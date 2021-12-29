from django.urls import path

from . import views


app_name = 'pizzapasta'
urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/', views.PizzaIndexView.as_view(), name='Pizza'),
    path('pizza/<int:pk>/', views.PizzaDetailView.as_view(), name='PizzaDetail'),
    path('pasta/', views.PastaIndexView.as_view(), name='Pasta'),
    path('pasta/<int:pk>/', views.PastaDetailView.as_view(), name='PastaDetail')
]
