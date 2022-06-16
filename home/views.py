from django.shortcuts import render

# Create your views here.


def index(request):
    """ This view renders the index page, a new user's first interaction with the site."""

    return render(request, 'home/index.html')
