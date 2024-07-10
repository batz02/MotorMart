from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = "chat"

urlpatterns = [
    path('chat_list', views.chat_list, name='chat_list'),  
    path('<int:chat_id>', views.chat_view, name='chat_view'),
    path('create_chat/<int:user_id>/', views.create_chat, name='create_chat'),
]