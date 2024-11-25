from django.http import HttpResponse
from django.shortcuts import render

# methods or routs
def home(request) :
    # return HttpResponse("Hello, kartikey. You are at home page.")
    return render(request , 'index.html')

def about(request) :
    return HttpResponse("Hello, kartikey. You are at about page.")

def contact(request) :
    return HttpResponse("Hello, kartikey. You are at contact page.")