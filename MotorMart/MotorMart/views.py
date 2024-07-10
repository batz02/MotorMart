from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import *
from annunci.models import Annuncio
from recensioni.models import Recensione


def home(request):
    marche = set()
    modelli = set()
    anni = set()

    for annuncio in Annuncio.objects.all():
        marche.add(annuncio.marca)
        modelli.add(annuncio.modello)
        anni.add(annuncio.anno)

    marche_list = sorted(list(marche))
    modelli_list = sorted(list(modelli)) 
    anni_list = sorted(list(anni), reverse=True) 

    context = {
        'marche': marche_list,
        'modelli': modelli_list,
        'anni': anni_list,
    }

    return render(request, "home.html", context)


class UserCreateView(CreateView):
    form_class = CreateUser
    template_name = "user_create.html"
    success_url = reverse_lazy("login")


@login_required
def profile(request):

    annunci = Annuncio.objects.filter(utente=request.user).order_by('marca', 'modello')
    recensioni = Recensione.objects.filter(venditore=request.user)

    context = {
        'annunci': annunci,
        'recensioni': recensioni
    }
    
    return render(request, "profile.html", context)


@login_required
def get_profile(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404()

    annunci = Annuncio.objects.filter(utente=user).order_by('marca', 'modello')
    recensioni = Recensione.objects.filter(venditore=user)

    context = {
        'annunci': annunci,
        'recensioni': recensioni
    }
    
    return render(request, "profile.html", context)

