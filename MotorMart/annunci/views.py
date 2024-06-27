from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

# Create your views here.

class ListingsView(ListView):
    model = Annuncio
    template_name = "annunci/cars.html"


def details(request,pk):
    annuncio = Annuncio.objects.get(id=pk)
    ctx = { "annuncio" : annuncio }
    return render(request,"annunci/details.html", ctx)