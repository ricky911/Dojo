from django.shortcuts import render, HttpResponse

def index(request):
	response = 'Response'
	return HttpResponse(reponse)

def index(request):
	return render(request, 'myapps/index.html')

def testimonials(request):
	return render(request, 'myapps/testimonials.html')

# Create your views here.
