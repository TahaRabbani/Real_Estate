# I HAVE CREATED THIS FILE
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     params = {'name': 'Taha', 'place':'london'}
#     return render (request, 'index.html', params)
#     # return HttpResponse ('''<h1>Real Estate</h1> <a href= "https://www.zameen.com/Property/karachi_mehmoodabad_flat_for_sale_1st_floor_brand_new-51195832-9201-1.html"> Beautifull flat at mehmoodabad karachi</a>
#     #                     <a href= "http://127.0.0.1:8000/removepunc"> 2 bedroom flat</a>
#     #                     <a href= "http://127.0.0.1:8000/capitalizefirst"> 3 bedroom flat</a>
#     #                     <a href= "http://127.0.0.1:8000/newlineremove"> 4 bedroom flat</a>
#     #                     <a href= "http://127.0.0.1:8000/spaceremove"> Furnished flat</a>
#     #                     <a href= "http://127.0.0.1:8000/charcount"> 2 story mansion</a>''')

# # def about(request):
# #     return HttpResponse ("about real estate")

# def removepunc(request):
#     return HttpResponse ("2 bedroom flat <a href= '/'>home</a>")

# def capfirst(request):
#     return HttpResponse ("3 bedroom flat <a href= '/'>home</a>")

# def newlineremove(request):
#     return HttpResponse ("4 bedroom flat <a href= '/'>home</a>")

# def spaceremove(request):
#     return HttpResponse ("Furnished flat <a href= '/'>home</a>")

# def charcount(request):
#     return HttpResponse ("2 story mansion <a href= '/'>home</a>")


# Importing the render function from Django's shortcuts module
# 'render' is used to generate and return an HTTP response with a specified template   
from django.shortcuts import render
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html')
# Plots view function
# Handles requests to the plots page
# Renders the 'pages/plots.html' template
def plots(request):
    return render(request, 'pages/plots.html')

def contact(request):
    return render(request, 'pages/contact.html')

@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to CSV file
        file_path = 'static/user_data.csv'  # Change to your desired path
        try:
            with open(file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([full_name, email, message])
        except Exception as e:
            return HttpResponse(f"Error saving message: {e}", status=500)

        return HttpResponse("Message sent successfully!", status=200)
    
    return HttpResponse("Invalid request method.", status=400)