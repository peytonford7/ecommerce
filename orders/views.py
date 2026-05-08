from django.shortcuts import render

# Create your views here.
def orders_home(request):
    return render(request, "orders_home.html")