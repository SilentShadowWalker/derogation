from django.shortcuts import render
from .models import City

# Create your views here.
def home(request):
    cities = City.objects.all() #This to get all record stored in the table wilaya
    return render(request, 'new_derogation.html', {'cities': cities})

def logIn(request):
    return render(request, 'login.html')

def suivi(request):
    return render(request, 'suividerogation.html')