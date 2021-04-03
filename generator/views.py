from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):


    characters = list('abcdefghijklomnopqstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('uppercase'):
        characters.extend(list('!@#$%^&*()'))



    length = int(request.GET.get("length",12))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)


    return render(request,'generator/password.html',{'password':thepassword})
