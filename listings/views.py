from django.shortcuts import render
from django.http import HttpResponse

def dummy(request):
    return HttpResponse("<h1>Congrats, you reached the dummy view</h1>")
