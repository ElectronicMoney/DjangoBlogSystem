from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Welcome To The Blog Home Page!</h1>')

def about(request):
    return HttpResponse('<h1>Welcome To About Page!</h1>')