from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Rongo says hey there partner! <br/> <a href = '/rongo/about/' > About </a>")
    context_dict = {'boldmessege': 'I am bold context :D'}
    return  render(request,'rongo/index.html',context=context_dict)


def about(request):
    # return HttpResponse("Rongo says here is about page! <br/> <a href = '/rongo/' > Index </a>")
    context_dict = {'name': 'Ahmad Al-Sajid'}
    return render(request,'rongo/about.html',context=context_dict)
