# I HAVE CREATED THIS FILE
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse ('''<h1>Real Estate</h1> <a href= "https://www.zameen.com/Property/karachi_mehmoodabad_flat_for_sale_1st_floor_brand_new-51195832-9201-1.html"> Beautifull flat at mehmoodabad karachi</a>
                        <a href= "http://127.0.0.1:8000/removepunc"> 2 bedroom flat</a>
                        <a href= "http://127.0.0.1:8000/capitalizefirst"> 3 bedroom flat</a>
                        <a href= "http://127.0.0.1:8000/newlineremove"> 4 bedroom flat</a>
                        <a href= "http://127.0.0.1:8000/spaceremove"> Furnished flat</a>
                        <a href= "http://127.0.0.1:8000/charcount"> 2 story mansion</a>''')

# def about(request):
#     return HttpResponse ("about real estate")

def removepunc(request):
    return HttpResponse ("2 bedroom flat <a href= '/'>home</a>")

def capfirst(request):
    return HttpResponse ("3 bedroom flat <a href= '/'>home</a>")

def newlineremove(request):
    return HttpResponse ("4 bedroom flat <a href= '/'>home</a>")

def spaceremove(request):
    return HttpResponse ("Furnished flat <a href= '/'>home</a>")

def charcount(request):
    return HttpResponse ("2 story mansion <a href= '/'>home</a>")
    