from django.shortcuts import render, redirect, HttpResponse
import datetime

# def index(request):
# 	response = 'Response'
# 	return HttpResponse(response)

def index(request):
	time = {
	'day' : datetime.datetime.now()
	}
	return render(request, 'main/index.html', time)
# Create your views here.