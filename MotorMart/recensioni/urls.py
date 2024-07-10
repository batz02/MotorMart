from django.urls import path
from .views import *

app_name = "recensioni"

urlpatterns = [
    path("inserisci/<int:pk>", review, name='review'),
]
