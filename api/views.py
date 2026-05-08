from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def admin(request):
    return render(request, "admin.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")

def logout(request):
    return render(request, "logout.html")