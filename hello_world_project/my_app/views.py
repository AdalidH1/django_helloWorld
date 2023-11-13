from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hola mundo, me llamo Adalid")
# Create your views here.
