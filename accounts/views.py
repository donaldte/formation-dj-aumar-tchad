from django.shortcuts import render
from .models import CustomUser
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


#view base sur les fonction de django
# les vue base sur les classe generic view(tu dois definier ton formulaire)
# les fonction view base sur les classe 


"""
class AccountUserCreation(CreateView):
    model = CustomUser
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    template_name = 'account/register.html'
    success_url = '/account/login/'
    form_class = UserFormClass
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Account created successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'An error occured')
        return super().form_invalid(form)
"""



class AccountUserCreation(View):
    
    template_name = 'account/register.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    data = {}
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        
        if password != password2:
            messages.error(request, 'Password mismatch')
            return render(request, self.template_name)
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        
        
        if len(username) < 3:
            messages.error(request, 'Username must be at least 3 characters')
        
        try:
        
            CustomUser.objects.create_user(email=email, password=password, 
                                           username=username, first_name=first_name,
                                           last_name=last_name
                                           )
            messages.success(request, 'Account created successfully')
            return render(request, self.template_name)
        except Exception as e:
            messages.error(request, 'An error occured')
        data = {
            'email': email,
            'username': username,
            'firstname': first_name,
            'lastname': last_name,
        }
        return render(request, self.template_name, data)
    



class AccountUserLogin(View):
    
    template_name = 'account/login.html'
    
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    
    def post(self, request, *args, **kwargs):
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email does not exist')
            return render(request, self.template_name)    
        
        user = authenticate(email=email, password=password)
        
        if user is None:
            messages.error(request, 'Invalid credentials')
            return render(request, self.template_name)
        else:
            login(request, user)
            messages.success(request, 'Login successful')
            return render(request, self.template_name)
        
        


class AccountUserLogout(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'account/logout.html')        