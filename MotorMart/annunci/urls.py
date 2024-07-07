from django.urls import path
from .views import *

app_name = "annunci"

urlpatterns = [
    path("", ListingsView.as_view(), name="annunci_list"),
    path("search", search, name="search"),
    path("inserisci/", create, name="create"),
    path("<pk>/", details, name="details"),
]