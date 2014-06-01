from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return render(request, 'cc101/loading_page.html')

def testing(request):
   return render(request, 'cc101/index.html')   

def cc101_view(request):
    return HttpResponse("Welcome to CurioCity 101. Please take our awesome course!")

def cclab_view(request):
    return HttpResponse("Welcome to CurioCity Lab. Become a mad scientist")

def medhini(request):
	return render(request, 'cc101/medhini.html') 
# Create your views here.
