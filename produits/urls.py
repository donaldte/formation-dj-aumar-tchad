from django.urls import path 
from . import views

app_name = 'produits'

urlpatterns = [
    path('', views.home, name='acceuil'),
    path('create/', views.create_blog_view, name='create_blog')
]
