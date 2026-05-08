from django.shortcuts import render

# Create your views here.
def products_home(request):
    return render(request, "products_home.html")