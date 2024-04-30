from django.contrib import messages,auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import loginTable, UserProfile
# Create your views here.

def RegisterUser(request):
    if request.method=='POST':
        username=request.POST.get('username')
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('password1')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This user already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                 user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,
                                           email=email,password=password)
            user.save()
            return redirect('login')
        else:
            messages.info(request,'This password is not matching')
            return redirect('register')
    return render(request,'auth/registration.html')

def LoginUser(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('createbook')
            else:
                messages.info(request,'Please provide correct details')
                return redirect('login')
        return render(request,'auth/login.html')


@login_required
def admin_view(request):

    return render(request,'admin/book.html')


def log_out(request):
    auth.logout(request)
    return redirect('login')
