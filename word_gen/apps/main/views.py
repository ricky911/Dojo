from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
	return render(request, 'main/index.html')

def generate(request):
	random_word = get_random_string(length=14)
	print random_word
	if 'count' not in request.session:
		request.session['count'] = 1
	else:
		request.session['count'] += 1
	# if request.method == 'POST':
	# 	request.session['count'] = 1
	# else:
	# 	request.session['count'] += 1
	request.session['word'] = random_word
	return redirect('/')