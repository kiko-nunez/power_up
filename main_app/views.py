from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Station, Vehicle
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import requests
from .forms import StationForm, SearchForm, VehicleForm
import uuid
import boto3

url = "https://electric-vehicle-charging-station-and-point.p.rapidapi.com/us/elec.json"

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

@login_required
def stations_index(request):
    stations = Station.objects.all()
    data = []
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search_value = form.cleaned_data['search_value']
            querystring = {
            "orderBy": "\"postcode\"",
            "equalTo": f"\"{search_value}\"",
            "print": "\pretty\"",
            "limitToFirst": "5",
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring)
            data = response.json()
        else:
            print("bad form")
            # return render(request, 'stations/index.html', {'form': form})
    else:
        form = SearchForm()
    return render(request, 'stations/index.html', {'form': form, 'stations': stations, 'data': data})

@login_required
def stations(request):
    stations = Station.objects.all()
    return render(request, 'stations/stations.html', {'stations': stations})

@login_required
def add_station(request, station_id):
    form = StationForm(request.POST)
    if form.is_valid():
        new_station = form.save(commit=False)
        new_station.station_id = station_id
        new_station.save()
    return redirect('detail', station_id=station_id)

    # stations = Station.objects.filter()
    # return render(request, 'stations/stations.html', {'stations': stations})

@login_required
def stations_detail(request, station_id):
    station = Station.objects.get(id=station_id)
    return render(request, 'stations/detail.html', {'station': station})
@login_required
def store_api_data():
    pass
@login_required
def vehicle_index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_index.html', {'vehicles': vehicles})
@login_required
def add_vehicle(request, vehicle_id):
    form = VehicleForm(request.POST)
    if form.is_valid():
        new_vehicle = form.save(commit=False)
        new_vehicle.vehicle_id = vehicle_id
        new_vehicle.save()
    return redirect('vehicle_index', vehicle_id=vehicle_id)
@login_required
def vehicle_detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})

def add_photo(request, vehicle_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, vehicle_id=vehicle_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', vehicle_id=vehicle_id)


# Classes Below

class StationCreate(LoginRequiredMixin, CreateView):
    model = Station
    fields = 'name', 'address', 'availability', 'connectors', 'reviews'
    success_url = '/mystations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class StationUpdate(LoginRequiredMixin, UpdateView):
    model = Station
    fields = '__all__'


class StationDelete(DeleteView):
    model = Station
    success_url = '/stations/'

#Vehicle Classes

class VehicleCreate(LoginRequiredMixin, CreateView):
    model = Vehicle
    fields = '__all__'
    success_url = '/vehicles/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'


class VehicleDelete(LoginRequiredMixin, DeleteView):
    model = Vehicle
    success_url = '/vehicles/'






