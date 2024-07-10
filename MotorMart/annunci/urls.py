from django.urls import path
from .views import *

app_name = "annunci"

urlpatterns = [
    path("", ListingsView.as_view(), name="annunci_list"),
    path("search", search, name="search"),
    path("inserisci/", create, name="create"),
    path("modifica/<int:pk>", edit, name="edit"),
    path("elimina/<int:pk>", delete, name="delete"),
    path("acquista/<int:pk>", buy, name="buy"),
    path("<int:pk>", details, name="details"),
]
