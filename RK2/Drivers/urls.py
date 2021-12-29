from django.urls import path

from . import views


app_name = 'Drivers'
urlpatterns = [
    path('', views.index, name='index'),
    path('drivers/', views.DriverListView.as_view(), name='drivers'),
    path('drivers/<int:pk>/', views.DriverDetailView.as_view(), name='driver_detail'),
    path('drivers/add/', views.DriverCreateView.as_view(), name='driver_add'),
    path('driver/<int:pk>/edit', views.DriverUpdateView.as_view(), name='driver_edit'),
    path('driver/<int:pk>/delete', views.DriverDeleteView.as_view(), name='driver_delete'),
    path('carstations/', views.CarstationListView.as_view(), name='carstations'),
    path('carstations/add/', views.CarstationCreateView.as_view(), name='carstation_add'),
    path('carstations/<int:pk>/edit', views.CarstationUpdateView.as_view(), name='carstation_edit'),
    path('carstations/<int:pk>/delete', views.CarstationDeleteView.as_view(), name='carstation_delete'),
    path('report/', views.report, name='report')
]
