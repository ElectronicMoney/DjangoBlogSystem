from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = {
       'posts': [
               {
                'id': 1,
                'author': 'Emeka Augustine',
                'title': 'Nigerian is a corrupt country!',
                'body': 'The level of corruption in Nigeria is unbearable.'
            },
            {
                'id': 2,
                'author': 'Ben James',
                'title': 'Ghana is a corrupt country!',
                'body': 'The level of corruption in Ghana is too bad.'
            }
       ]
    }
    return render(request, 'home.html', posts)

def about(request):
    return render(request, 'about.html')