from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUser(UserCreationForm):
    def save(self, commit=True):
        user = super().save(commit) 
        return user
