from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.contrib import messages


def home(request, *args, **kwargs):
    blogs = Blog.objects.all()
    messages.info(request, 'Welcome to our blog')
    context = {
        'blogs': blogs
    }
    return render(request, "index.html", context)


def create_blog_view(request, *args, **kwargs):
    forms = BlogForm(request.POST, request.FILES)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Blog created successfully')
        redirect('products:acceuil')
    else:
        messages.error(request, 'An error occured {}'.format(forms.errors))
    
    context = {
        'forms': forms
    }
    return render(request, "create_blog.html", context)