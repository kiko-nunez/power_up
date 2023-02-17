from django.test import TestCase
from main_app.forms import StationForm, SearchForm, VehicleForm
from main_app.models import Station, Vehicle


class TestForms(TestCase):
    def setUp(self):
        self.station = Station.objects.create(
            name="Test Station",
            address="123 Test St",
            availability=1,
            connectors="Chademo, CCS",
            reviews="Test Review",
        )
        self.vehicle_data = {
            "type": "BEV",
            "make": "Tesla",
            "model": "Model S",
            "batterysize": 85,
        }

# This test checks if a valid StationForm is valid by creating a form with valid data and asserting that it is valid.
    def test_station_form_valid_data(self):
        form = StationForm(
            data={
                "name": "Test Station",
                "address": "123 Test St",
                "availability": 1,
                "connectors": "Chademo, CCS",
                "reviews": "Test Review",
            }
        )
        self.assertTrue(form.is_valid())

#This test checks if an invalid StationForm with no data is invalid by creating a form with no data and asserting that it is not valid, and that there are 5 errors.
    def test_station_form_no_data(self):
        form = StationForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)

# This test checks if a valid SearchForm is valid by creating a form with a valid search_value and asserting that it is valid.
    def test_search_form_valid_data(self):
        form = SearchForm(data={"search_value": "EC1V 0AH"})
        self.assertTrue(form.is_valid())
# This test checks if an invalid SearchForm with no data is invalid by creating a form with no data and asserting that it is not valid, and that there is 1 error.
    def test_search_form_no_data(self):
        form = SearchForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

