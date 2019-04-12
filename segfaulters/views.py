from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps
Listing = apps.get_model('listings', 'Listing')



def home(request):
	return render(request, 'home.html')

def profile(request):
    return render(request, 'userprofile.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')