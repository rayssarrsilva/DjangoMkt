#from django.http import HttpResponse
from django.shortcuts import render 
from django.views.generic.base import TemplateView

def homepage(request):
    #return HttpResponse("Hello world, you are in the homepage")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("u are in the about apge")
    return render(request, 'about.html')

def suporte(request):
    return render(request, 'support.html')
 