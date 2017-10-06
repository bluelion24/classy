from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("Hello, world you're at the Polls index.")

    
# Create your views here.
