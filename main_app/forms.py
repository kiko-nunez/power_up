from django.forms import ModelForm
from .models import Station
from django import forms

class StationForm(ModelForm):
  class Meta:
    model = Station
    fields = ['name', 'address', 'availability', 'connectors', 'reviews']

class SearchForm(forms.Form):
    search_value = forms.CharField(label='Post Code', max_length=100)

        