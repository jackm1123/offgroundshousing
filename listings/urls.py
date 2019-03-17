from django.urls import path

from . import views

app_name = 'listings'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("<int:listing_id>/",views.one_listing, name="one_listing")
]
