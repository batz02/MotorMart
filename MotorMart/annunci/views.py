from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

# Create your views here.

class ListingsView(ListView):
    model = Annuncio
    template_name = "annunci/cars.html"