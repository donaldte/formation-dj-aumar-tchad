from django.db import models

from accounts.models import CustomUser

class Action(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    
class Reference(models.Model):
    email = models.EmailField()
    number_of_references = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.email
    
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name    
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
"""
une api CRUD SUR LA TABLE  CHATFORUM QUI EST EN MANY TO MANY AVEC LA TABLE CUSTOMUSER
"""    

class ChatForum(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(CustomUser)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    