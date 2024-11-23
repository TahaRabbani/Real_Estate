# I HAVE CREATED THIS FILE
from django.http import HttpResponse

def index(request):
    return HttpResponse ("<h1>Real Estate</h1>")

def about(request):
    return HttpResponse ("about real estate")