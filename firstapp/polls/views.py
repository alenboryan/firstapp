import re
from django.shortcuts import render, redirect
from django.contrib.auth import login , logout , authenticate
from django.http import HttpResponse , HttpResponseRedirect
from .models import  PollUser , Addinfo
from django.contrib.auth.models import User
from bs4 import BeautifulSoup
from .forms import AddinfoForm




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
        
    if firstname == username or lastname == username:
        return render(request, "polls/error.html")
        
        
    while True:
        if (len(password)<=8):
            flag = -1
            break
        elif not re.search("[a-z]", password):
            flag = -1
            break
        elif not re.search("[A-Z]", password):
            flag = -1
            break
        elif not re.search("[0-9]", password):
            flag = -1
            break
        elif not re.search("[_@$]" , password):
            flag = -1
            break
        else:
            flag = 0
            user = User.objects.create_user(username=username, password=password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            PollUser(user=user).save()
            return redirect("/polls/login")
    if flag == -1:
        return redirect("/polls/error")
    
def log_out(request):
    logout(request)
    return HttpResponseRedirect("/polls/login")

def python_introduction(request):
    return render(request, "polls/intro.html")

def python_syntax(request):
    return render(request, "polls/syntax.html")

def error(request):
    return render(request, "polls/error.html")



def create(request):
    error = ''
    if request.method == 'POST':
        form = AddinfoForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success URL or return a success message
            return HttpResponseRedirect('/polls/')  # Redirect to a success URL
        else:
            error = 'Creating failed. Please check the form data.'
    else:
        form = AddinfoForm()  # Create an instance of the form for GET requests
    
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'polls/create.html', data)


def add_info(request):
    info = Addinfo.objects.all()
    return render(request, 'polls/info.html',{"info":info})