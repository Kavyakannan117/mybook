from django.contrib import messages,auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import loginTable, UserProfile
# Create your views here.


def userRegistration(request):
    login_table=loginTable()
    userprofile=UserProfile()

    if request.method=='POST':
        userprofile.username=request.POST['username']
        userprofile.password=request.POST['password']
        userprofile.password2=request.POST['password1']

        login_table.username=request.POST['username']
        login_table.password=request.POST['password']
        login_table.password2=request.POST['password1']
        login_table.type='user'

        if request.POST['password']==request.POST['password1']:
            userprofile.save()
            login_table.save()

            messages.info(request,'Registration Success')
            return redirect('login')
        else:
            messages.info(request,'Password is not matching')
            return redirect('register')
    return render(request,'auth/registration.html')



def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=loginTable.objects.filter(username=username,password=password,type='user').exists()
        print(user)

        try:
            if user is not None:
                user_details=loginTable.objects.get(username=username,password=password)
                user_name=user_details.username
                type=user_details.type

                if type=='user':
                    request.session['username']=user_name
                    return redirect('user_view')
                elif type=='admin':
                    request.session['username']=user_name
                    return redirect('admin_view')

            else:
                messages.info(request,'invalid username or password')

        except:
            messages.info(request,'invalid credentials')

    return render(request,'auth/login.html')

@login_required
def admin_view(request):
    user_name=request.session.get('username',None)
    return render(request,'auth/admin_view.html',{'user_name':user_name})

def user_view(request):
    user_name=request.session.get('username')
    return render(request,'auth/user_view.html',{'user_name':user_name})

def log_out(request):
    logout(request)
    return redirect('login')
