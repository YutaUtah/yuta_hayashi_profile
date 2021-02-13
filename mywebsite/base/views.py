from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.

def home(request):
	return render(request, 'base/home.html')

def dog_pics(request):
	return render(request, 'base/other_templates/dog_page.html')

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")