from django import http
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from . models import UserProfile
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "login.html")

def insurance(request):
    return render(request, "login.html")

def resources(request):
    return render(request, "login.html")

def contact(request):
    return render(request, "login.html")



def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        type = request.POST['type']

        try:
            uobj = User(first_name=firstname, last_name=lastname, username=username, password=make_password(password), email=email)
            uobj.save()

            user_pro_obj = UserProfile(user=uobj, usertype=type, mobile=mobile)
            user_pro_obj.save()
            return redirect("/login/")

        except:
            pass

    return render(request,"signup.html")



def login_cl(request):
    if request.method == "POST":
        uname = request.POST['uname']
        pwd = request.POST['pwd']

        User = authenticate(username=uname, password=pwd)
        if User:
            login(request,User)
            #user---> role(agent/client)
            #request.user

            #profileobj = User.objects.get(user__username=request.user)
            if User.is_superuser == False:
                return redirect('/client/home/')
            
            elif User.is_superuser == True:
                return redirect('/agent/home/')

        else:
            return HttpResponse("<h1> Login again </h1>")

    return render(request, "login.html")

def logout_cl(request):
    logout(request)
    return redirect('/login/')


