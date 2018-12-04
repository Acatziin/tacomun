from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Holaaaaaa')

def hola(request,name):
    return HttpResponse('Hola{}'.format(name))    