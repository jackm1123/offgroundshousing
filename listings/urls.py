from django.urls import path

from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.list_of_listings, name='list_of_listings'),
    path("<int:listing_id>/", views.one_listing, name="one_listing"),
    path("<int:listing_id>/condensed", views.one_listing_condensed, name="one_listing_condensed"),
    path("<int:listing_id>/slides", views.one_listing_slides, name="one_listing_slides"),
    #path("<int:listing_id>/inactive", views.one_listing_inactive, name="one_listing_inactive"),

]
