from django.shortcuts import render, redirect, HttpResponse

def index(request):
	response = 'Response'
	return HttpResponse(response)

def index(request):
	return render(request, 'myapps/index.html')

def projects(request):
	return render(request, 'myapps/projects.html')

def about(request):
	return render(request, 'myapps/about.html')

def testimonials(request):
	return render(request, 'myapps/testimonials.html')

def hello(request):
	if request.method == "POST":
		print '*' * 50
		print request.method
		print request.POST
		print '*' * 50
		request.session['name'] = request.POST['first_name']
		return redirect('/')
	else:
		return redirect('/')

# Create your views here.
