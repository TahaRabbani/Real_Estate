# django framework 
from django.shortcuts import render
import csv
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# its for user when they access the home page
def home(request):
    return render(request, 'index.html')
# its for user when they access the plots page
def plots(request):
    return render(request, 'pages/plots.html')

def contact(request):
    return render(request, 'pages/contact.html')
# it will retrieve the data from user and stores it in csv file
@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # error handling
        # Save to CSV file
        file_path = 'static/user_data.csv'  
        try:
            with open(file_path, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([full_name, email, message])
        except Exception as e:
            return HttpResponse(f"Error saving message: {e}", status=500)

        return HttpResponse("Message sent successfully!", status=200)
    
    return HttpResponse("Invalid request method.", status=400)