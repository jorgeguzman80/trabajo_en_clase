from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'layout_home/home.html')