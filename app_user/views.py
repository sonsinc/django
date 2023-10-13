from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if  username=='' or email=='' or password=='':
            messages.warning(request,'Please enter all fields')
            return redirect('/register')
        else:
            if User.objects.filter(username=username).exists():
                messages.warning(request,'The user already exists')
                return redirect('/register')
            else:
                user=User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                messages.success(request,'Create account successfully')
                return redirect('/register')
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=='' or password=='':
            messages.warning(request, 'Please enter all fields.')    
            return redirect('/login')
        else:
            user=auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.warning(request,'Account information not found.')
                return redirect('/login')
    else:
        return render(request, 'login.html')
        
def logout(request):
    auth.logout(request)
    return redirect('/login')
    
def profile(request):
    pass
def edit_profile(request):
    pass