from django.shortcuts import render
def home(request):
# 	return render(request, 'index.html')
	return render(request, 'home.html')
def profile(request):
    return render(request, 'userprofile.html')
