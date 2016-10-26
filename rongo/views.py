from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Rongo says hey there partner! <br/> <a href = '/rongo/about/' > About </a>")


def about(request):
    return HttpResponse("Rongo says here is about page! <br/> <a href = '/rongo/' > Index </a>")
