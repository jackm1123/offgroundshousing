from django.urls import path

from . import views

app_name = 'listings'
urlpatterns = [
    path('listings/', views.IndexView.as_view(), name='index'),
    path('', views.index)
]
