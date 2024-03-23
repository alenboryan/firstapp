from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import login , logout , authenticate
from django.http import HttpResponse , HttpResponseRedirect
from .models import  PollUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from bs4 import BeautifulSoup
import requests



def index(request):
    return render(request, 'polls/index.html')

def about(request):
    return render(request, 'polls/about.html')


def login(request):
    if request.method == 'GET':
        return render(request, "polls/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]

        print(username, password)

        user = authenticate(username=username, password=password)

        if user:
            return HttpResponseRedirect("/polls/")
        else:
            return render(request, "polls/login", context={"error": "wrong login or password"})

def register(request):
    if request.method == 'GET':
        return render(request, "polls/register.html")

    else:
        
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST['password']
        
        user = User.objects.create_user(username=username, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()

        PollUser(user=user).save()

        return HttpResponseRedirect("/polls/login")
    

def log_out(request):
    logout(request)
    return HttpResponseRedirect("/polls/login")

def python_introduction(request):
    url = 'https://www.w3schools.com/python/python_intro.asp'
    req = requests.get(url)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    all_info = soup.find_all(class_="w3-clear nextprev")
    print(all_info)
    return render(request, 'polls/intro.html', {'all_info': all_info})
