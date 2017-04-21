from django.shortcuts import render, HttpResponse

def index(response):
	response ="request!"
	return HttpResponse(request)

def index(request):
	return render(request, 'app1/index.html')

# Create your views here.
