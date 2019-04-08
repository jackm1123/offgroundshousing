from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.usr, name='usr'),
    path('dashboard', views.dashboard, name='dashboard'),

]
