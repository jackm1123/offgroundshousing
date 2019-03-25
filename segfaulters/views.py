from django.shortcuts import render
from django.core.mail import send_mail


def home(request):
# 	return render(request, 'index.html')
	return render(request, 'index.html')

def profile(request):
    return render(request, 'userprofile.html')
