from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from .models import Listing

class IndexView(generic.ListView):
    template_name = 'listings/list_of_listings.html'
    context_object_name = 'list_of_listings'

    def get_queryset(self): # pragma no cover (not sure how to test)
        return Listing.objects.all()

def one_listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        "listing" : listing,
    }
    return render(request, 'listings/page_for_one_listing.html', context)

def one_listing_condensed(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        "listing" : listing,
    }
    return render(request, 'listings/one_listing_condensed.html', context)

# Deleted: I think this code isn't used
# def index(request):
#     return render_to_response('home/index.html')
