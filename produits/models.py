from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import CustomUser
from django.db.models import Q, F, Count, Sum, Avg, Max, Min

class Product(models.Model): #outer class
    name = models.CharField(max_length=13)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    quantity = models.IntegerField(default=0)
    
    class Meta: # inner 
        # concept metadata information sur la donnee
        verbose_name = 'Produits'
        ordering = ['price']
        


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
            
        
class Blog(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    """
    CASCADE: supprime les objets liés
    PROTECT: refuse la suppression de l'objet lié
    SET_NULL: définit la clé étrangère sur NULL
    SET_DEFAULT: définit la clé étrangère sur sa valeur par défaut
    SET(): définit la clé étrangère sur la valeur donnée
    DO_NOTHING: ne fait rien
    """
    
    class Meta:
        verbose_name = 'Blog'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title       
    
    
    def get_image(self):
        if self.image:
            return self.image.url
        return None 


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comment'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.content
    
    def get_user(self):
        return self.user.email
    
    def get_blog(self):
        return self.blog.title

