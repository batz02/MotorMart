from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recensione
from django.contrib import messages
from django.contrib.auth.models import User
from annunci.models import Annuncio
from django.contrib.auth.decorators import login_required

@login_required
def review(request, pk):
    annuncio = get_object_or_404(Annuncio, pk=pk)
    venditore = annuncio.utente
    if request.user.id == venditore.id:
        messages.success(request, "Non puoi recensire te stesso")
        return redirect('annunci:details', pk=pk)

    existing_review = Recensione.objects.filter(recensore=request.user, venditore=venditore).first()
    if existing_review:
        messages.success(request, "Hai già recensito il venditore")
        return redirect('annunci:details', pk=pk)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        descrizione = request.POST.get('descrizione',' ') 
        recensione = Recensione(
            recensore=request.user,
            venditore=venditore,
            descrizione=descrizione if descrizione else None, 
            rating=rating
        )
        recensione.save()
        messages.success(request, "Recensione inserita")
        return redirect('annunci:details', pk=pk)
    return render(request, 'recensioni/submit_review.html', {'venditore': venditore})
