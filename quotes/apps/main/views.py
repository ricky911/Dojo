# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def currentUser(request):
	if 'user_id' in request.session:
		return User.objects.get(id=request.session['user_id'])

def index(request):
	return render(request, 'main/index.html')

def register(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		# print check['status']
		if check['status'] == True:
			user = User.objects.registerUser(request.POST)
			request.session['user_id'] = user.id
			return redirect('/success')
		else:
			for error in check['errors']:
				messages.add_message(request, messages.ERROR, error, extra_tags='register')
				return redirect('/')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.loginUser(request.POST)
		# print check['status']
		if check['status'] == True:
			request.session['user_id'] = check['user'].id
			return redirect('/success')
		else:
			messages.add_message(request, messages.ERROR, 'Invalid credentials', extra_tags='login')
			return redirect('/')

def indexQuote(request):
	user = currentUser(request)
	context = {
	'quotes': Quote.objects.order_by('-created_at').all().exclude(favorite=user),
	'favorites': Quote.objects.order_by('-created_at').all(),
	'currentUser': user
	}
	return render(request, 'main/success.html', context)

def addQuote(request):
	if request.method != 'POST':
		return redirect('/success')
	else:
		check = Quote.objects.validateQuote(request.POST)
		if check['status'] == True:
			user = currentUser(request)
			quote = Quote.objects.addQuote(request.POST, user)
			return redirect('/success')
		else:
			for error in check['errors']:
				messages.add_message(request, messages.ERROR, error)
				return redirect('/success')

def addFav(request, id):
	user = currentUser(request)
	quote = Quote.objects.get(id=id)
	user.favorited.add(quote)
	return redirect('/success')

def delFav(request, id):
	user = currentUser(request)
	quote = Quote.objects.get(id=id)
	user.favorited.remove(quote)
	return redirect('/success')

def profile(request, id):
	user = User.objects.get(id=id)
	context = {
	'this_user': user,
	'currentUser': currentUser(request),
	'quotes': Quote.objects.order_by('-created_at').all(),
	'count': Quote.objects.all().count()
	}
	return render(request, 'main/users.html', context)

def logout(request):
	request.session.clear
	return redirect('/')
