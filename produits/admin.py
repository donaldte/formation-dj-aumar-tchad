from django.contrib import admin
from .models import Product, Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at', 'updated_at']
    list_per_page = 10
    
    
admin.site.register(Blog, BlogAdmin)    