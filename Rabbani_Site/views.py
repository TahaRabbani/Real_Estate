# I HAVE CREATED THIS FILE
from django.http import HttpResponse

def index(request):
    return HttpResponse ('''<h1>Real Estate</h1> <a href= "https://www.zameen.com/Property/karachi_mehmoodabad_flat_for_sale_1st_floor_brand_new-51195832-9201-1.html"> Beautifull flat at mehmoodabad karachi</a>''')

# def about(request):
#     return HttpResponse ("about real estate")

def removepunc(request):
    return HttpResponse ("remove punc")

def capfirst(request):
    return HttpResponse ("capitalizefirst")

def newlineremove(request):
    return HttpResponse ("newlineremove")

def spaceremove(request):
    return HttpResponse ("spaceremove")

def charcount(request):
    return HttpResponse ("charcount")
    