from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def LOGIN(request):
    return render(request,'auth/login.html')

def REGISTER(request):
    return render(request,'auth/register.html')

@login_required(login_url="login")
def CHATROOM(request):
    user = request.user
    context = {
        'user':user
    }
    return render(request,'user/index.html',context)


def SAVEUSER(request):
    if request.method == 'POST':
        user = request.user
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        if user is not None:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            messages.success(request,'Profile updated successfully.')
            return redirect('room')
    else:
        messages.warning(request, 'Invalid request method.')
        return redirect('room') 
        

def DOLOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('room') 
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login') 
    else:
        return render(request, 'auth/login.html')


def DOREGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if UserProfile.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already taken.')
            return redirect('register')
        elif UserProfile.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already taken.')
            return redirect('register')
        else:
            user = UserProfile.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')  
    else:
        messages.warning(request, 'Invalid request method.')
        return redirect('register') 
    

def LOGOUT(request):
    logout(request)
    messages.success(request, 'Logout successfully. Please login again.')
    return redirect('login')