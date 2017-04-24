from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
	return render(request, 'main/index.html')

def create(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect('/')
		else:
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				first_name = request.POST.get('first_name'),
				last_name = request.POST.get('last_name'),
				email = request.POST.get('email'),
				password = hashed_pw,
				# confirm = request.POST.get('cpw'),
			)
			request.session['user_id'] = user.id
			messages.success(request, 'Success! Welcome, ' + request.POST.get('first_name') + '!')
			return render(request, 'main/success.html')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		user = User.objects.filter(email = request.POST.get('email')).first()
		# print request.POST.get('password')
		if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
				request.session['user_id'] = user.id
				messages.success(request, 'Success! Welcome, ' + user.first_name + '!')
				return render(request, 'main/success.html')
		else:
			messages.error(request, 'Email or password is not valid')
			return redirect('/')

# Create your views here.
