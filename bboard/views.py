from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Здесь будет выведен список объявлений.")


def hello(request):
    return HttpResponse("Hello!")

# Create your views here.
