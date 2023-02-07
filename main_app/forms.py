from django.forms import ModelForm
from .models import Station
from django import forms

class StationForm(ModelForm):
  class Meta:
    model = Station
    fields = ['name', 'address', 'availability', 'connectors', 'reviews']

class SearchForm(ModelForm):
    class Meta:
        model: Station
        fields = '__all__'