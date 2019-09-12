from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Anime is trash so I am...</h1>")

def komunikat(request):
    return HttpResponse("<h1>Skrrrrrrrr</h1>")

def hehe(request):
    return HttpResponse("<h1>hehe</h1>")