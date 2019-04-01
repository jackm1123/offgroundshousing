from django.core.mail import send_mail
from django.http import QueryDict
from django.views import generic
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext
from .models import Listing

class IndexView(generic.ListView):
    template_name = 'listings/list_of_listings.html'
    context_object_name = 'list_of_listings'

    def get_queryset(self): # pragma no cover (not sure how to test)

        objects = Listing.objects.all()

        def apply_GET_filter(arg_name,filter_name):
            nonlocal objects
            filter = self.request.GET.get(filter_name)
            kwargs = {arg_name: filter}
            if(filter != None):
                objects = objects.filter(**kwargs)

        apply_GET_filter("price__gte","price_low")
        apply_GET_filter("price__lte","price_high")
        apply_GET_filter("rating__gte","rating_low")
        apply_GET_filter("rating__lte","rating_high")
        apply_GET_filter("square_footage__gte","sqft_low")
        apply_GET_filter("square_footage__lte","sqft_high")
        apply_GET_filter("bedroom_num__gte","beds_low")
        apply_GET_filter("bedroom_num__lte","beds_high")
        apply_GET_filter("name","name")
        apply_GET_filter("phone_num","phone_num")
        apply_GET_filter("laundry_info","laundry")
        apply_GET_filter("parking_info","parking")
        apply_GET_filter("ownership_info","owned")
        apply_GET_filter("ownership_info","owned")

        # submission_date
        # active
        # favorite


        return objects

def one_listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
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

def one_listing_slides(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id)
    context = {
        "listing" : listing,
    }
    return render(request, 'listings/one_listing_slides.html', context)

def one_listing_inactive(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    listing.active = False
    print("here")
    send_mail(
        'Hello a listing you were interested in went down: ' + listing.name,
        'this is an automated message do not reply',
        'segfaulters3240@gmail', ['djx7et@virginia.edu'], fail_silently=False)
    for i in listing.user_list.all():
        send_mail(
            'Hello a listing you were interested in went down: ' + listing.name,
            'this is an automated message do not reply',
            'segfaulters3240@gmail', [i.email], fail_silently=False)
    context = {
        "listing" : listing,
    }
    return render(request, 'listings/page_for_one_listing.html', context)
# Deleted: I think this code isn't used
# def index(request):
#     return render_to_response('home/index.html')
