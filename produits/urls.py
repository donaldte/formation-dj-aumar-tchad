from django.urls import path 
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.home, name='acceuil')
]
