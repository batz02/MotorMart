from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from annunci.models import Annuncio


def home(request):
    
    marche = set()
    modelli = set()
    anni = set()
    
    for annuncio in Annuncio.objects.all():
        marche.add(annuncio.marca)
        modelli.add(annuncio.modello)
        anni.add(annuncio.anno)
    
    marche_list = list(marche)
    modelli_list = list(modelli)
    anni_list = list(anni)
    print(anni_list)
    
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
