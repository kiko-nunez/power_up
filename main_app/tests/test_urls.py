from django.test import SimpleTestCase
from django.test import TestCase
from main_app.models import Station
from django.urls import reverse, resolve
from main_app.views import home, about, stations, signup, add_vehicle, vehicle_detail, vehicle_index, stations_index, stations_detail, add_station, StationUpdate, StationCreate, StationDelete, VehicleCreate, VehicleUpdate, VehicleDelete

class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_signup_url_is_resolved(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func, signup)    

    def test_stations_url_is_resolved(self):
        url = reverse('stations')
        print(resolve(url))
        self.assertEquals(resolve(url).func, stations)    

    def test_station_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, stations_index)   

    def test_station_detail_url_is_resolved(self):
        url = reverse('detail', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func, stations_detail)   

    def test_station_create_url_is_resolved(self):
        url = reverse('stations_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, StationCreate)

    def test_station_update_url_is_resolved(self):
        url = reverse('stations_update', args=['0'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, StationUpdate)

    def test_station_delete_url_is_resolved(self):
        url = reverse('stations_delete', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, StationDelete)
    
    def test_add_station_url_is_resolved(self):
        url = reverse('add_station', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_station)  

    def test_vehicle_index_url_is_resolved(self):
        url = reverse('vehicle_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, vehicle_index)  

    def test_vehicle_detail_url_is_resolved(self):
        url = reverse('vehicle_detail', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func, vehicle_detail)  

    def test_vehicle_create_url_is_resolved(self):
        url = reverse('vehicle_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, VehicleCreate)  

    def test_add_vehicle_url_is_resolved(self):
        url = reverse('add_vehicle', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_vehicle)  

    def test_vehicle_update_url_is_resolved(self):
        url = reverse('vehicle_update', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, VehicleUpdate)  

    def test_vehicle_delete_url_is_resolved(self):
        url = reverse('vehicle_delete', args=[0])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, VehicleDelete)  