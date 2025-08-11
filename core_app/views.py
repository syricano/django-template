from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "core_app/home.html")

def about(request):
    return render(request, "pages/about.html")

def contact(request):
    return render(request, "pages/contact.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # go to Sign In after successful signup
    else:
        form = UserCreationForm()
    return render(request, "auth/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "auth/profile.html")
