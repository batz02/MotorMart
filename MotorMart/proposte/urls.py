from django.urls import path
from . import views

app_name = "proposte"

urlpatterns = [
    path('<int:pk>/', views.listing_detail, name='proposals'),
    path('accept/<int:proposal_id>/', views.accept_proposal, name='accept_proposal'),
    path('reject/<int:proposal_id>/', views.reject_proposal, name='reject_proposal'),
]
