from django.test import TestCase
from main_app.models import Station, Vehicle

class StationModelTest(TestCase):

    def setUp(self):
        self.station = Station.objects.create(
            name = 'Test Station',
            address = '123 Test Street',
            availability = '24/7',
            connectors = 'Level 2',
            reviews='Great station'
        )

    def test_station_name(self):
        self.assertEquals(self.station.name, 'Test Station')


class VehicleModelTest(TestCase):

    def setUp(self):
        self.vehicle = Vehicle.objects.create(
            type='BEV',
            make='Tesla',
            model='Model S',
            batterysize=85
        )

#tests whether the Vehicle object is created correctly and its string representation is correct.
    def test_vehicle_creation(self):
        self.assertTrue(isinstance(self.vehicle, Vehicle))
        self.assertEqual(self.vehicle.__str__(), f'{self.vehicle.make} {self.vehicle.model}')

#tests whether the type field is limited to the choices specified in TYPES.
    def test_vehicle_type_choices(self):
        vehicle = Vehicle.objects.get(id=self.vehicle.id)
        types = dict(Vehicle.TYPES)
        self.assertEqual(vehicle.type, 'BEV')
        for key, value in types.items():
            vehicle.type = key
            vehicle.save()
            self.assertEqual(vehicle.type, key)

#tests whether the max length of the model field is 25.
    def test_vehicle_make_length(self):
        max_length = self.vehicle._meta.get_field('make').max_length
        self.assertEqual(max_length, 25)

#tests whether the max length of the model field is 25.
    def test_vehicle_model_length(self):
        max_length = self.vehicle._meta.get_field('model').max_length
        self.assertEqual(max_length, 25)

#tests whether the verbose name of the batterysize field is correct.
    def test_vehicle_batterysize_verbose_name(self):
        batterysize_field = self.vehicle._meta.get_field('batterysize')
        self.assertEqual(batterysize_field.verbose_name, 'Battery Size')

#tests whether the batterysize field is an integer.
    def test_vehicle_batterysize_type(self):
        batterysize_field = self.vehicle._meta.get_field('batterysize')
        self.assertEqual(batterysize_field.get_internal_type(), 'IntegerField')
