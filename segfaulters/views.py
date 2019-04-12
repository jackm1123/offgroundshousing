from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps
Listing = apps.get_model('listings', 'Listing')
UserProfile = apps.get_model('users', 'UserProfile')



def home(request):
	return render(request, 'home.html')

def profile(request):
    objects = Listing.objects.all()
    profile = UserProfile.get_user(request.user.username)
    return render(request, 'userprofile.html', {'list_of_listings': objects,'UserProfile' : profile})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
