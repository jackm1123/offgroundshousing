from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Listing

class IndexView(generic.ListView):
    template_name = 'listings/list_of_listings.html'
    context_object_name = 'list_of_listings'

    def get_queryset(self):
        return Listing.objects.all()

def dummy(request):
    return HttpResponse("<h1>Congrats, you reached the dummy view</h1>")

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))