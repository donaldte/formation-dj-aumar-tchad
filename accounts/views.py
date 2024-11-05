from django.shortcuts import render
from .models import CustomUser
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import Permission, Group

"""
group_vendeurs = Group.objects.create(name='vendeurs')
group_editors = Group.objects.create(name='editors')
group_admins = Group.objects.create(name='admins')
group_superusers = Group.objects.create(name='superusers')
group_customers = Group.objects.create(name='customers')

add permission to group
group_vendeurs.permissions.add(Permission.objects.get(codename='add_blog'))
group_editors.permissions.add(Permission.objects.get(codename='add_blog'))
group_admins.permissions.add(Permission.objects.get(codename='add_blog'))
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
        
            user = CustomUser.objects.create_user(email=email, password=password, 
                                           username=username, first_name=first_name,
                                           last_name=last_name
                                           )
            user.user_permissions.add(Permission.objects.get(codename='add_blog'))
            
            # add to group (profile_editors)
            user.groups.add(Group.objects.get(name='profile_editors'))
            
            user.save()
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
            # check if the user has add blog permission before login
            if user.has_perm('produits.add_blog'): # app_name.codename
                #verify si l'utilisateur est dans le groupe profile_editors
                # if user.groups.filter(name='profile_editors').exists():
                #     login(request, user)
                #     messages.success(request, 'Login successful')
                # else:
                #     messages.error(request, 'You are not allowed to login')
                # has_perms(['app_name.codename', 'app_name.codename'])
                login(request, user)
                messages.success(request, 'Login successful')
            else:
                messages.error(request, 'You do not have permission to login')    
            return render(request, self.template_name)
        
        


class AccountUserLogout(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'account/logout.html')        