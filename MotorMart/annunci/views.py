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
def details(request, pk):
    annuncio = Annuncio.objects.get(id=pk)
    ctx = {"annuncio": annuncio}
    return render(request, "annunci/details.html", ctx)


def search(request):
    if request.method == "POST":
        anno = request.POST.get('anno')
        marca = request.POST.get('marca')  # Updated field name
        modello = request.POST.get('modello')
        chilometraggio = request.POST.get('chilometraggio')
        prezzo = request.POST.get('prezzo')

        # Construct the filter dictionary
        filter_kwargs = {}
        if anno:
            filter_kwargs['anno'] = anno
        if marca:
            filter_kwargs['marca'] = marca
        if modello:
            filter_kwargs['modello'] = modello
        if chilometraggio:
            filter_kwargs['chilometraggio'] = chilometraggio
        if prezzo:
            filter_kwargs['prezzo'] = prezzo

        annunci_filtered = Annuncio.objects.filter(**filter_kwargs)
        return render(request, "annunci/cars.html", {'object_list': annunci_filtered})


def create(request):
    if request.method == 'POST':
        form = CreaAnnuncio(request.POST, request.FILES)
        if form.is_valid():
            annuncio = form.save(commit=False)
            annuncio.utente = request.user
            annuncio.save()
            return redirect('annunci:annunci_list')
        else:
            print(form.errors)  # Debug line to print form errors
    else:
        form = CreaAnnuncio()
    
    return render(request, "annunci/create.html", {'form': form})