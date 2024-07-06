from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

class ListingsView(ListView):
    model = Annuncio
    template_name = "annunci/cars.html"

@login_required
def details(request,pk):
    annuncio = Annuncio.objects.get(id=pk)
    ctx = { "annuncio" : annuncio }
    return render(request,"annunci/details.html", ctx)


def search(request):

    if request.method == "POST":

        anno = request.POST.get('anno')
        marchio = request.POST.get('marchio')
        modello = request.POST.get('modello')
        chilometraggio = request.POST.get('chilometraggio')
        prezzo = request.POST.get('prezzo')

        print(anno)
        return render(request,"annunci/cars.html")
        return HttpResponse(f"Searched for: Anno={anno}, Marchio={marchio}, Modello={modello}, Chilometraggio={chilometraggio}, Prezzo={prezzo}")


def create(request):
    
    return render(request,"annunci/create.html")