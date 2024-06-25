from django.urls import path
from .views import *

app_name = "annunci"

urlpatterns = [
    path("", annunci_list, name="annunci_list"),
    
]