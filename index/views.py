from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from music.models import Music

def home(request):
    welcome = "Welcome to ABC Musical Store"
    return render(request, 'index/home.html', {'welcome' : welcome})

def author(request):
    author = "Bernardo"
    return render(request, 'index/author.html', {'author' : author})
