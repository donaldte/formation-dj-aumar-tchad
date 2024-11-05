
from django.contrib.auth.models import Permission, Group
from django.shortcuts import render
from django.views import View
from accounts.models import CustomUser
from django.contrib import messages

# permssions booleenne 

# def hom_view(request):
#     if request.user.is_authenticated:
#         if request.user.is_superuser:
#             return render(request, 'superuser.html')
#         else:
#             return render(request, 'home.html')
#     return render(request, 'home.html')


# permissions avec has_perm et has_perms

class UserPermissionWhenCreatinAccount(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, 'account/register.html')
    
    
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        username = request.POST.get('username')
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        
        if password != password2:
            messages.error(request, 'Password mismatch')
            return render(request, 'account/register.html')
        
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
            # give some permissions to the user
            user.user_permissions.add(Permission.objects.get(codename='add_blog'))
            
            # add to group (profile_editors)
            user.groups.add(Group.objects.get(name='profile_editors'))
            
            user.save()
            
            messages.success(request, 'Account created successfully')
            return render(request, 'account/register.html')
        except Exception as e:
            messages.error(request, 'An error occured')
        data = {
            'email': email,
            'username': username,
            'firstname': first_name,
            'lastname': last_name,
        }
        return render(request, 'account/register.html', data)