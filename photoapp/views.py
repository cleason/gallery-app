from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, "photoapp/home.html")

def about(request):
    return render(request, "photoapp/about.html")


def contact(request):
    return render(request, "photoapp/contact.html")