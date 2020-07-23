from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    password = ""
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    
    if request.GET.get('specialCharacter'):
        characters.extend('!@#$%^&*()')
    
    if request.GET.get('numbers'):
        characters.extend('1234567890')

    for i in range(length):
        password += random.choice(characters)
    return render(request, 'generator/pass.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')