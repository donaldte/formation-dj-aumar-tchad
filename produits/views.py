from django.shortcuts import render
from django.http import HttpResponse
# wsgi 

# CRUD models produit en utilisant fonctions , classe generics, fonction dans les classe

def home(request, *args, **kwargs):
    return HttpResponse('<h1> Bonjour tous le monde </h1>')