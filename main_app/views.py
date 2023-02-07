from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Station
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from .forms import StationForm

url = "https://electric-vehicle-charging-station-and-point.p.rapidapi.com/us/elec.json"

querystring = {"orderBy":"\"postcode\"","equalTo":"\"80212\"","print":"\"pretty\"","limitToFirst":"1"}

headers = {
	"X-RapidAPI-Key": "2eba11bd42msh3cdfe07ccc61a1cp13ef6bjsn84cf6ca7c03a",
	"X-RapidAPI-Host": "electric-vehicle-charging-station-and-point.p.rapidapi.com"
}
# print(response.text)


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


def stations_index(request):
    data = ""
    stations = Station.objects.all()
    if request.method == 'POST':
        form = StationForm(request.POST)
        if form.is_valid():
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()
            print(response.text)
            return render(request, 'stations/index.html', { 'form': form})
    else:
        form = StationForm()
    return render(request, 'stations/index.html', {'stations': stations, 'data': data})

def stations(request):
    stations = Station.objects.all()
    return render(request, 'stations/stations.html', {'stations': stations})

def add_station(request, station_id):
    form = StationForm(request.POST)
    if form.is_valid():
        new_station = form.save(commit=False)
        new_station.station_id = station_id
        new_station.save()
    return redirect('detail', station_id=station_id)    
    
    
    # stations = Station.objects.filter()
    # return render(request, 'stations/stations.html', {'stations': stations})
    


def stations_detail(request, station_id):
  station = Station.objects.get(id=station_id)
  return render(request, 'stations/detail.html', { 'station': station })

#Classes Below

class StationCreate(CreateView):
    model = Station
    fields = 'name', 'address', 'availability', 'connectors', 'reviews'
    success_url = '/mystations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class StationUpdate(UpdateView):
    model = Station
    fields = '__all__'
class StationDelete(DeleteView):
    model = Station
    success_url = '/stations/'


