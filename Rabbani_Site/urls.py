"""
URL configuration for Rabbani_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# import admin from django framework
from django.contrib import admin
# import paths
from django.urls import path, include

from . import views

urlpatterns = [
    # the path setting for admin 
    path('admin/', admin.site.urls),
    # the path setting for home 
    path('', views.home, name='home'),
    # the path setting for plots
    path('plots/', views.plots, name='plots'),
    # the path setting for contact
    path('contact/', views.contact, name='contact'),
    # the path setting for send messages in contact page
    path('send-message/', views.send_message, name='send_message'),
]  


