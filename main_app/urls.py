from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('stations/', views.stations_index, name='index'),
    path('mystations/', views.stations, name='stations'),
    path('stations/<int:station_id>/', views.stations_detail, name='detail'),
    path('stations/create/', views.StationCreate.as_view(), name='stations_create'),
    path('stations/<int:station_id>/add_station/', views.add_station, name='add_station'),
    path('stations/<int:pk>/update/', views.StationUpdate.as_view(), name='stations_update'),
    path('stations/<int:pk>/delete/', views.StationDelete.as_view(), name='stations_delete'),
    path('vehicles/', views.vehicle_index, name='vehicle_index'),
    path('vehicles/<int:vehicle_id>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicles/create/', views.VehicleCreate.as_view(), name='vehicle_create'),
    path('vehicles/<int:vehicle_id>/add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('vehicles/<int:pk>/update/', views.VehicleUpdate.as_view(), name='vehicle_update'),
    path('vehicles/<int:pk>/delete/', views.VehicleDelete.as_view(), name='vehicle_delete'),
]
