from django.shortcuts import render, redirect

def index(request):
	print 'reached index.html'
	return render(request, 'main/index.html')

def results(request):
	print 'reached results.html'
	return render(request, 'main/results.html')

def process(request):
	print 'reached process(redirects to results)'
	if request.method == 'POST':
		print request.POST
		data = {
			'name': request.POST['name'],
			'location': request.POST['location'],
			'language': request.POST['language'],
			'comment': request.POST['comment']
		}
		request.session['user'] = data
		
		return redirect('/results')


# Create your views here.
