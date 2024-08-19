from django import forms
from .models import Room
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RoomForm(forms.ModelForm):
    class Meta:
        model=Room
        fields='__all__'

class Register(UserCreationForm):
    class Meta:
        model=User
        fields=('username','password1','password2')