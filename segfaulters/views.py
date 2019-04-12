from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps
Listing = apps.get_model('listings', 'Listing')



def home(request):
# 	return render(request, 'index.html')
	return render(request, 'home.html')

def profile(request):
	objects = Listing.objects.all()
	return render(request, 'userprofile.html', {'list_of_listings': objects})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
