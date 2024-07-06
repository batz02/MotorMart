from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *


def home(request):
    return render(request, template_name="home.html")


class UserCreateView(CreateView):
    form_class = CreateUser
    template_name = "user_create.html"
    success_url = reverse_lazy("login")
