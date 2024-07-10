from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import *
from .forms import *


class ListingsView(ListView):
    model = Annuncio
    template_name = "annunci/cars.html"
    ordering = ['marca', 'modello']
    context_object_name = 'annunci'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marche = set()
        modelli = set()
        anni = set()

        for annuncio in Annuncio.objects.all():
            marche.add(annuncio.marca)
            modelli.add(annuncio.modello)
            anni.add(annuncio.anno)

        context['marche'] = list(marche)
        context['modelli'] = list(modelli)
        context['anni'] = list(anni)

        return context


@login_required
def details(request, pk):
    annuncio = Annuncio.objects.get(id=pk)
    ctx = {"annuncio": annuncio}
    return render(request, "annunci/details.html", ctx)


def search(request):

    if request.method == "POST":

        anno = request.POST.get('anno')
        marchio = request.POST.get('marchio')
        modello = request.POST.get('modello')
        chilometraggio = request.POST.get('chilometraggio')
        prezzo = request.POST.get('prezzo')

        filter_kwargs = {}
        if anno:
            filter_kwargs['anno'] = anno
        if marchio:
            filter_kwargs['marca'] = marchio
        if modello:
            filter_kwargs['modello'] = modello
        if chilometraggio:
            try:
                if '-' in chilometraggio:
                    min_chilometraggio, max_chilometraggio = map(int, chilometraggio.split('-'))
                    filter_kwargs['chilometraggio__gte'] = min_chilometraggio
                    filter_kwargs['chilometraggio__lte'] = max_chilometraggio
                else:
                    min_chilometraggio = int(chilometraggio)
                    filter_kwargs['chilometraggio__gte'] = min_chilometraggio
            except ValueError:
                pass
        if prezzo:
            try:
                if '-' in prezzo:
                    min_prezzo, max_prezzo = map(int, prezzo.split('-'))
                    filter_kwargs['prezzo__gte'] = min_prezzo
                    filter_kwargs['prezzo__lte'] = max_prezzo
                else:
                    min_prezzo = int(prezzo)
                    filter_kwargs['prezzo__gte'] = min_prezzo
            except ValueError:
                pass

        annunci_filtered = Annuncio.objects.filter(**filter_kwargs)
        return render(request, "annunci/cars.html", {'object_list': annunci_filtered})

@login_required
def create(request):
    if request.method == 'POST':
        form = CreaAnnuncio(request.POST, request.FILES)
        if form.is_valid():
            annuncio = form.save(commit=False)
            annuncio.utente = request.user
            annuncio.save()
            messages.success(request, "Annuncio inserito correttamente")
            return redirect('annunci:annunci_list')
        else:
            messages.error(request, "Errore nell'inserimento dell'annuncio")
            return redirect('annunci:annunci_list')
    else:
        form = CreaAnnuncio()
        return render(request, "annunci/create.html", {'form': form})



@login_required
def edit(request, pk):

    annuncio = get_object_or_404(Annuncio, pk=pk)

    if annuncio.utente != request.user:
        messages.error(request, "Non hai i permessi per modificare questo annuncio")
        return redirect('annunci:annunci_list')

    if request.method == 'POST':
        form = CreaAnnuncio(request.POST, request.FILES, instance=annuncio)
        if form.is_valid():
            annuncio = form.save(commit=False)
            annuncio.utente = request.user
            annuncio.save()
            messages.success(request, "Annuncio modificato correttamente")
            return redirect('annunci:details', pk=annuncio.pk)
    else:
        form = CreaAnnuncio(instance=annuncio)

    return render(request, "annunci/edit.html", {'form': form})


@login_required
def delete(request, pk):
    annuncio = get_object_or_404(Annuncio, pk=pk)
    
    if annuncio.utente != request.user:
        messages.error(request, "Non hai i permessi per modificare questo annuncio")
        return redirect('annunci:annunci_list')
    
    if request.method == "POST":
        annuncio.delete()
        messages.success(request, "Annuncio eliminato correttamente")
        return redirect('annunci:annunci_list')

    return render(request, "annunci/delete.html" , {'annuncio': annuncio})


@login_required
def buy(request,pk):

    annuncio = get_object_or_404(Annuncio, pk=pk)

    if annuncio.utente == request.user:
        messages.error(request, "Non hai i permessi per modificare questo annuncio")
        return redirect('annunci:details', pk=annuncio.pk)
    
    if annuncio.venduto == True:
        messages.error(request, "Auto già venduta")
        return redirect('annunci:details', pk=annuncio.pk)
    
    if request.method == "POST":

        annuncio.venduto = True
        annuncio.prezzo_acquisto = annuncio.prezzo
        annuncio.compratore = request.user.id
        annuncio.save()

        messages.error(request, "Auto acquistata correttamente")
        return redirect('annunci:details', pk=annuncio.pk)
    
    return render(request, "annunci/buy.html" , {'annuncio': annuncio})
