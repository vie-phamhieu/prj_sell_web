from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def index(request):
    return render(request, 'home_page/index.html')