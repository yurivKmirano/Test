from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest


# Create your views here.
# Listado de vehiculos

def menu(request):
    return render(request,'core/menu.html')

def registro(request):
    return render(request,'core/registro.html')

def login(request):
    return render(request,'core/login.html')








