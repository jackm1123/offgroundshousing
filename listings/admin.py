from django.contrib import admin

from .models import Listing,Listing_Image,Review

admin.site.register(Listing)
admin.site.register(Listing_Image)
admin.site.register(Review)



# class Listing_ImageInline(admin.TabularInline):
#     model = Listing_Image
#     extra = 3
#
# class ListingAdmin(admin.ModelAdmin):
#     inlines = [ Listing_ImageInline, ]
