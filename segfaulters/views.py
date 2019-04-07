from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.apps import apps
listing = apps.get_model('listings', 'Listing')


def home(request):
# 	return render(request, 'index.html')
	return render(request, 'home.html')

def profile(request):
    return render(request, 'userprofile.html')

def search(request):
    if 'query' in request.GET and request.GET['query']:
        q = request.GET['query']
        q = q.strip()
        props = listing.objects.filter(name__icontains=q)
        return render(request, 'listings/list_of_listings.html',
                      {'list_of_listings': props, 'query': q})

    else:
        return HttpResponse('None Found Sorry')
