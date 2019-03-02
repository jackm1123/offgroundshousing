from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Listing

class IndexView(generic.ListView):
    template_name = 'listings/list_of_listings.html'
    context_object_name = 'list_of_listings'

    def get_queryset(self):
        return Listing.objects.all()
