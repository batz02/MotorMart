from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),  # Show the list of users on the home page
    path('chat/<int:chat_id>/', views.chat_view, name='chat_view'),
    path('create_chat/<int:user_id>/', views.create_chat, name='create_chat'),
]