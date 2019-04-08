from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404, render


# Create your views here.

def dashboard(request):
    return render(request, 'users/dashboard.html',{})

def usr(request):
    return render(request,'users/usr.html',{})
