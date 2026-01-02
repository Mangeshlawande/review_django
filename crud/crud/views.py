from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Helo World, You are at About Page")

def contact(request):
    return HttpResponse("Helo World, You are at Contact Page")

def service(request):
    return HttpResponse("Helo World, You are at Service Page")

