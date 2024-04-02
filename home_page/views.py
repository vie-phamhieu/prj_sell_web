from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def homepage(request):
    return render(request, 'home_page/home.html')