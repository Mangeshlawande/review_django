from django.http import HttpResponse



def home(request):
    return HttpResponse("Hello World You are at home page. ")

def about(request):
    return HttpResponse("Helo World, You are at About Page")

def contact(request):
    return HttpResponse("Helo World, You are at Contact Page")

def service(request):
    return HttpResponse("Helo World, You are at Service Page")

