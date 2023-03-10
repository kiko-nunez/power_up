from django.forms import ModelForm
from .models import Station, Vehicle
from django import forms

class StationForm(ModelForm):
  class Meta:
    model = Station
    fields = ['name', 'address', 'availability', 'connectors', 'reviews']

class SearchForm(forms.Form):
    search_value = forms.CharField(label='Postcode', max_length=100)

class VehicleForm(forms.ModelForm):
  class Meta: 
    model: Vehicle
    fields = '__all__'

        