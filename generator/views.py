from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):

    return render(request, 'generator/home.html', {'password': '%%@^@svssbbsb'})

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('special'):
        characters.extend(list('#%&*$@'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    

    length = int(request.GET.get('length'))
    thepassword = ''
    
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html', {'name': 'Kweku' , 'lastName': 'Don'})

def contactus(request):
    return render(request, 'generator/contactus.html')

