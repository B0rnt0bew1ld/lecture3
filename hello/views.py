from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def varun(request):
    return HttpResponse("Hello, Varun!")

def devil(request):
    return HttpResponse("Hello, Devil!")

def greet(request, name):
    return render(request, "hello/greet.html",
                  {
                      "name" : name.capitalize()
                  })