from django.db import models


class Product(models.Model): #outer class
    name = models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    
    class Meta: # inner 
        # concept metadata information sur la donnee
        verbose_name = 'Produits'
        ordering = ['price']
