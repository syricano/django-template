from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

