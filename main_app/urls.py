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
    path('stations/<int:station_id>/add_station/', views.add_station, name='add_station')
]
