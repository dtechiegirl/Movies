# from email import message
import email
from django.shortcuts import redirect, render, redirect
from django.http import HttpRequest, HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout

from .models import Movie, Registration
from django.contrib import messages
from .models import Movie
# def home(request):
#     return HttpResponse( "<h1>hello world</h1>")

# def home(request):
#     return render(request, "index.html")



def index(request):
    movies = Movie.objects.all()

    return render(request, "index-2.html", {'movies': movies})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        # if User.objects.filter(username=username).exist():
        #     message.info(request, 'Username already exist')
        #     return redirect('register')
        if password != password2:
            messages.info(request, 'password does not match')
            return redirect('register')
        else:
            user = Registration.objects.create(username=username, password = password)
            user.save();
            return redirect('login')
    return render(request, 'register.html')
# def register(request):
#     if request.method == 'get':
#         name = request.GET['name']
#         password = request.GET['password']
#         password2 = request.GET['password2']
#         if password == password2:
#             user = User.objects.create_user(name=name, password = password2)
#             user.save();
#         return redirect('login')
#     return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        # email = request.POST['email']
        # user = auth.authenticate(username= username, password= password)
        user = Registration.objects.filter(username=username, password=password).first()
        # user = Registration.authenticate(username=username, password=password).first()
        if user and user.username == username:
            return redirect('/')
        else: 
            messages.info(request, 'details invalid')
    return render(request, "index-2.html")

def logout(request):
    # auth.logout(request)
    django_logout(request)
    return redirect('/')


# Create your views here
  