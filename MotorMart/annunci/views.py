from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


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
        marchio = None
        modello = None
        chilometraggio = None
        prezzo = None

        annunci_filtered = Annuncio.objects.filter(
            anno=anno,
            marchio=marchio,
            modello=modello,
            chilometraggio=chilometraggio,
            prezzo=prezzo
        )

        print(annunci_filtered)

        return render(request,"annunci/cars.html", {'object_list': annunci_filtered})
        

def create(request):

    if request.method == 'POST':
        form = CreaAnnuncio(request.POST, request.FILES)
        if form.is_valid():
            annuncio = form.save(commit=False) 
            annuncio.utente = request.user  
            annuncio.save()
            return redirect('annunci:annunci_list')
    else:
        form = CreaAnnuncio()

    return render(request, "annunci/create.html", {'form': form})